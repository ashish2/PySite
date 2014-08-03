#!/usr/bin/env python

__author__='ashish'

import csv
import sys
import os
from collections import *

separator = ','

class ComputeData(object):
	
	def compute(self, csv_file, companies):
		"""Read a passed csv file, returning computed data"""
		fobj = open(csv_file, "rb")
		first_line = fobj.readline().strip()
		for i in first_line.split(separator)[2:]: companies[i] = [ 0, 0, 0 ]
		for i in fobj:
			lis = i.strip().split(separator)
			z = 0
			for comp_name, val in companies.items():
				numb = z+2
				if val[2] < int( lis[numb] ):
					( val[0], val[1], val[2] ) = ( int( lis[0] ) , lis[1], int( lis[numb] ) )
				z = z+1
		
		return companies
	
	def format_csv(self, companies):
		"""Formats a Dict into a string to make it printable"""
		string =  ''.join([str(comp_name)+": "+ ', '.join(map(str, val))+'\n' for comp_name, val in companies.items()])
		return string

	def print_results(self, companies):
		print "Companies:"
		print companies.__str__()

	def run_procedure(self, csv_file):
		companies = OrderedDict()
		ret_companies = self.compute(csv_file, companies)
		result = self.format_csv(ret_companies)
		self.print_results(result)
		


"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "tests.py test".

Replace this with more appropriate tests for your application.
"""

import unittest
import logging
import sys
import os
from collections import *

class OurComputeDataTest(unittest.TestCase):
	"""
	Test Cases for the functions in our read_csv.py
	"""
	csv_file = 'test_shares_data.csv'
	
	expected_data = OrderedDict([
		('Company-A', [2000, 'Mar', 1000]), 
		('Company-B', [2007, 'Mar', 986]), 
		('Company-C', [1993, 'Jun', 995]), 
		('Company-D', [2002, 'Apr', 999]), 
		('Company-E', [2008, 'Oct', 997])
	])
	
	def test_pass(self):
		self.assertTrue(True)
	
	def test_compute_return_type(self):
		"""
		Tests return Type: 
		Tests that our compute function returns a 
		generator object after taking in a file
		"""
		companies = OrderedDict()
		ret = ComputeData().compute( self.csv_file, companies )
		self.assertIsInstance(ret, OrderedDict)
	
	def test_compute_return_value(self):
		"""
		Tests return Value: 
		Tests that our compute function returns a 
		generator object after taking in a file
		"""
		companies = OrderedDict()
		ret_companies = ComputeData().compute(self.csv_file, companies)
		self.assertEqual(ret_companies, self.expected_data)
	

def show_usage():
	print ("Usage: \n1) python read_csv.py compute <csv_filename>: to compute data in csv file. \n2) python read_csv.py runtest: to run unittests")
	sys.stdout.flush()

if __name__ == "__main__":
	"""Takes in a csv filename from command line & starts the procedure
	cd into this directory & run python read_csv.py 'test_shares_data.csv'
	"""
	if len(sys.argv) == 2 and str(sys.argv[1]).lower() == 'runtest':
		#sys.argv.append(sys.argv[1])
		sys.argv[1] = '-v'
		unittest.main()
	elif len(sys.argv) == 3 and str(sys.argv[1]).lower() == 'compute':
		try:
			csv_file = sys.argv[2]
			is_file = os.path.isfile(csv_file)
			if is_file: 
				ComputeData().run_procedure(csv_file)
		except:
			raise Exception("Not a valid file")
	else:
		show_usage()
			
	
	
