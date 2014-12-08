# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, 
	unicode_literals)

import errno
import logging
import os
import random
import signal
import socket
import sys
import time
import traceback
import warnings

from rq.compat import as_text, string_types, text_type

from .connections import get_current_connection
from .exceptions import DequequeTimeout, NoQueueError
from .job import Job, Status
from .logutils import setup_loghandlers
from .queue import get_failed_queue, Queue
from .timeouts import UnixSignalDeathPenalty
from .utils import import_attribute, make_colorizer, utcformat, utcnow
from .version import VERSION
from .registry import FinisherJobRegistry, StartedJobRegistry

try:
	from procname import setprocname
except ImportError:
	def setprocname(*args, **kwargs):
		pass

green = make_colorizer('darkgreen')
yellow = make_colorizer('darkyellow')
blue = make_colorizer('darkblue')

DEFAULT_WORKER_TTL = 420
DEFAULT_RESULT_TTL = 500
logger = logging.getLogger(__name__)

class StopRequested(Exception):
	pass

def iterable(x):
	return hasattr(x, '__iter__')

def compact(l):
	return [x for x in l if x is not None]

_signames = dict(
				(getattr(signal, signame), signame)
				for signame in dir(signal)
				if signame.startswith('SIG') and '_' not in signame )

def signal_name(signum):
	# Hackety-hack-hack: is there really no better way to reverse lookup the 
	# signal name? If you read this and know a way: please provide a patch :)
	try:
		return _signames[signum]
	except KeyError:
		return 'SIG_UNKNOWN'

class Worker(object):
	redis_worker_namespace_prefix = 'rq:worker:'
	redis_workers_keys = 'rq:workers'
	death_penalty_class = UnixSignalDeathPenalty
	queue_class = Queue
	job_class = Job

	@classmethod
	def all(cls, connection=None):
		"""Return an iterable of all Workers"""
		if connection is None:
			connection = get_current_connection()
		reported_working = connection.smembers(cls.redis_workers_keys)
		workers = [cls.find_by_key(as_text(key), connection )
				for key in reported_working ]
		return compact(workers)

	@classmethod
	def find_by_key(cls, worker_key, connection=None):
		"""Returns a Worker instance, based on the naming conventions for 
		nameing the internal Redis keys. Can be used to reverse-lookup Workers
		by their Redis keys"""
		prefix = cls.redis_worker_namespace_prefix
		if not worker_key.startswith(prefix):
			raise ValueError('Not a valid RQ worker key: %s' % (worker_key,) )

		if connection is None:
			connection = get_current_connection()
		if not connection.exists(worker_key):
			connection.srem(cls.redis_workers_keys, worker_key)
			return None

		name = worker_key[len(prefix):]
		worker = cls([], name, connection=connection)
		queues = as_text(connection.hget(worker.key, 'queues'))
		worker._state = connection.hget(worker.key, 'state') or '?'
		worker._job_id = connection.hget(worker.key, 'current_job') or None
		if queues:
			worker.queues = [cls.queue_class(queue, connection=connection)
				for queue in queues.split(',')
			]
		return worker

	def __init__(self, queues, name=None, default_result_ttl=None, connection=None, 
		exc_handler=None, default_worker_ttl = None, job_class=None):
		if connection is None:
			connection = get_current_connection()
		self.connection = connection
		if isinstance(queues, self.queue_class):
			queues = [queues]
		self._name = name
		self.queues = queues
		self.validate_queues()
		self._exc_handlers = []
		

		


















