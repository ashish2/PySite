

### Singleton 1

# class Singleton(object):
# 	"""Singleton with instance stored in a single variable"""
# 	_dict = False
# 	def __new__(cls):
# 		if cls._dict:
# 			print "EXISTS"
# 			return cls._dict
# 		else:
# 			print "NEW"
# 			return super(cls.__class__, cls).__new__(cls)
# 	def __init__(self):
# 		print "INIT"
# 		self.__class__._dict = self
# 		print ""

# class Singleton(object):
# 	"""Singleton with instance stored inside a dict"""
# 	_dict = dict()
# 	def __new__(cls):
# 		# if 'key' in cls.__class__._dict:
# 		if 'key' in cls._dict:
# 			print "EXISTS"
# 			# return cls._dict['key']
# 			return type
# 		else:
# 			print "NEW"
# 			# return super(cls.__class__, cls).__new__(cls)
# 			return type
# 	def __init__(self):
# 		print "INIT"
# 		self._dict['key'] = self
# 		print ""


# a = Singleton()
# aa = Singleton()

# a.b = 1
# print a.b


# class Sing(object):
# 	__metaclass__ = Singleton

	
# a = Sing()
# print aa.b
# print dir(a)

# aa = Sing()
# print aa.b
# print dir(a)


### Singleton 2

# class Singleton(object):
# 	# __metaclass__ = Singleton
# 	def __init__(self, *args, **kwargs):
# 		self.x = 1
# 		self.y = 2
# 		super(Singleton, self).__init__(*args, **kwargs)
# 		self.__instance = None
# 	def __call__(self, *args, **kwargs):
# 		print "call"
# 		self.x = 3
# 		self.y = 4
# 		if self.__instance is None:
# 			# Ori
# 			# self.__instance = super(Singleton, self).__call__(*args, **kwargs)
# 			# Add
# 			self.__instance = super(Singleton, self).__init__(*args, **kwargs)
# 		return self.__instance

# a = Singleton()
# print a.x, a.y
# # a() using __call__ here
# a()
# print a.x, a.y


# =====================================

# class A:
# 	def f(self):
# 		return self.g()

# 	def g(self):
# 		return 'A'

# class B(A):
# 	def g(self):
# 		return 'B'

# a = A()
# b = B()
# print a.f(), b.f()
# print a.g(), b.g()


# =====================================

# Descriptor Protocol
# class Descrip(object):
# 	def __get__(self):
# 		pass

# 	def __set__(self):
# 		pass


# =====================================

# try:
# 	print 1.1
# except Exception, e:
# 	print "e"
# 	print e
# else:
# 	print "else"
# finally:
# 	print "finally"


# def f():
# 	try:
# 	    print "a"
# 	    # raise Exception("doom")
# 	    return
# 	except:
# 	    print "b"
# 	else:
# 	    print "c"
# 	finally:
# 	    print "d"

# f()

# =====================================

# class Var
# class A(object):
# 	# class variable
# 	a = 2
# 	def __init__(self):
# 		print "self"
# 		print self

# 	@staticmethod
# 	def statmeth():
# 		# print "statmeth"
# 		return 5

# 	@classmethod
# 	def clsmeth(cls):
# 		# print "clsmeth"
# 		# print cls
# 		return 4


# a = A()
# # b = A()
# # print a.a
# a.a = 3
# # print a.a
# # print b.a
# print dir(a)

# # print a.statmeth()
# # print A.clsmeth()

# =====================================


# class Employee:
# 	'Optional class docs'
# 	empCount = 0
# 	__d = 2

# 	def __init__(self, name, salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.empCount += 1
# 		print self.__dict__

# 	def displayCount(self):
# 		print "Total Employee %d" % Employee.empCount

# 	def displayEmployee(self):
# 		print "Name: %s, Salary: %d" % ( self.name, self.salary)

# 	def __del__(self):
# 		class_name = self.__class__.__name__
# 		print "Class %s deleted" % (class_name)

# 	def setAttr(self, attr, val):
# 		self.__dict__[attr] = val

# 	def getAttr(self, attr):
# 		return self.__dict__[attr]

# class Child(Employee):
# 	def setAttr(self, attr, val):
# 		self.__dict__[attr] = val + 10



# # e = Employee("a", 5)	
# a = Employee("b", 6)
# a.setAttr("c", 4)
# # print dir(a)
# print a.getAttr("c")

# print hasattr(a, "name")
# print getattr(a, "name")
# print getattr(a, "salary")

# print a.displayEmployee()
# print dir(Employee)

# print Employee.__dict__
# print a.__repr__()

# print type(str(a))
# print type(repr(a))

# print a._Employee__d
# a._Employee__d = 5
# print a._Employee__d


# b = a

# print a
# print b
# a = 4
# del a

# print a
# print b


# class Vector(object):
# 	__hid = 0
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
# 		Vector.__hid += 1

# 	def __str__(self):
# 		return "Vector(%s, %s)" % (self.a, self.b)

# 	def __add__(self, other):
# 		a = self.a + other.a
# 		b = self.b + other.b
# 		return Vector(a, b)


# v = Vector(3,4)
# vv = Vector(5,6)

# print v + vv
# print v._Vector__hid
# print vv._Vector__hid

# =====================================

# class Employee(object):
# 	empCount = 0
# 	def __init__(self, name, salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.empCount += 1

# 	def setAttr(self, attr, val):
# 		self.__dict__[attr] = val

# 	def getAttr(self, attr):
# 		return self.__dict__[attr]

# 	def hi(self):
# 		print "hi"

# 	@classmethod
# 	def clsmeth(cls):
# 		return cls

	# def __del__(self):
	# 	print self.__class__.__name__ , " instance destroyed"


# class Inher(Employee):
# 	def hi(self):
# 		print "child hi"

# print dir(Employee)
# print a.setAttr("o", 6)

# a = Employee("ash", 5)
# print id(Employee)
# print id(Employee.clsmeth())
# print id(a.clsmeth())

# b = Employee("bash", 55)
# print id(Employee.clsmeth())
# print id( b.clsmeth() )



# class Vector(object):
# 	__secretCount = 0
# 	def __init__(self, a, b):
# 		self.a = a 
# 		self.b = b
# 	def __str__(self):
# 		return "Vector(%s, %s)" % (self.a, self.b)
# 	def __add__(self, other):
# 		a = self.a + other.a
# 		b = self.b + other.b
# 		return Vector (a, b)
# 	def __sub__(self, other):
# 		print self
# 		print other
# 		a = self.a - other.a
# 		b = self.b - other.b
# 		return Vector(a, b)


# v = Vector(3,4)
# vv = Vector(5,6)
# print v-vv


# =====================================

class yrange():
	def __init__(self, n):
		self.i = 0
		self.n = n
	def __iter__(self):
		return self
	def next(self):
		if self.i < self.n:
			i = self.i
			self.i += 1
			return i
		else:
			raise StopIteration

y = yrange(3)

# print y.next()
# print y.next()
# print y.next()
# print y.next()
# print iter(y)
# print list(yrange(5))
# print sum(yrange(5))

# print list(y)
# print list(y)


class zrange():
	def __init__(self, n):
		self.i = 0
		self.n = n
	def __iter__(self):
		return zrange_iter(self.n)


# class zrange_iter():
# 	def __init__(self, n):
# 		self.i = 0
# 		self.n = n
# 	# Something seriously wrong with this iter
# 	def __iter__(self):
# 		""" *Check--- Something seriously wrong with this iter when used with iter() and list()"""
# 		if self.i < self.n:
# 			i = self.i
# 			self.i += 1
# 			return self
# 		else:
# 			raise StopIteration
# 	def next(self):
# 		"""*Check--- Something seriously wrong with this function when used with iter() and list()"""
# 		return self.i

### Using the above zrange(), zrange_iter() class with list() and iter() below
# z = zrange(5)
# print list(z)
# print iter(z)

# class zrange_iter():
# 	def __init__(self, n):
# 		self.i = 0
# 		self.n = n
# 	def __iter__(self):
# 		return self
# 	def next(self):
# 		if self.i < self.n:
# 			i = self.i
# 			self.i += 1
# 			return i
# 		else:
# 			raise StopIteration

# z = zrange(5)
# print list(z)
# print iter(z)


# class zzrange_iter():
# 	def __init__(self, n):
# 		self.i = 0
# 		self.n = n
# 	def __iter__(self):
# 		return self
# 	def next(self):
# 		if self.n-1 >= self.i:
# 			self.n = self.n-1
# 			return self.n
# 		else:
# 			raise StopIteration

# z = zzrange_iter(4)
# # print iter(z)
# # print z
# for i in z:
# 	print i


# =====================================

# Generators

# def yrange(n):
# 	print "begin"
# 	i = 0
# 	while i < n:
# 		print "before yield"
# 		yield i
# 		print "after yield", i
# 		i += 1
# 		print "incremented", i
# 	print "end"

# y = yrange(3)
# # print dir(y)
# print y.next()
# print y.next()
# print y.next()
# print y.next()
# for i in y:
# 	print i
# 	if i == 1:
# 		break


# Generator Expressions

# a = ( i for i in range(4) )
# print a.next()
# print a.next()
# print a.next()
# print a.next()
# print "Sum", sum(a)
# print sum( i for i in range(4) )
# print sum( i for i in range(4)  )

# li = [[1,2,3], [4,5,6]]

# def f(li):
# 	for i in li:
# 		print "1st"
# 		for k in i:
# 			print "2nd"
# 			yield k
# 			print ""
# 			print "yield 3rd"
# 		yield i
# 		print "4th"


# a = f(li)
# print a.next()
# print a.next()
# print a.next()
# print a.next()
# print a.next()


# =====================================

# RECURSION

# def fast_exp(x, n):
# 	if n == 0:
# 		print "if"
# 		return 1
# 	elif n % 2 == 0:
# 		print "elif"
# 		return fast_exp(x*x, n/2)
# 	else:
# 		print "else"
# 		return x * fast_exp(x, n-1)

# print fast_exp(2,4)

# =====================================

# THREADING

import threading, time

# exitFlag = 1
# class MyThread(threading.Thread):
# 	def __init__(self, threadID, name, counter, delay):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter
# 		self.delay = delay
# 	def run(self):
# 		print "Starting " + self.name + " time: "  + time.ctime(time.time())
# 		print_time(self.name, self.counter, self.delay)
# 		print "Exiting " + self.name
# 		# self.exit()

def print_time(threadName, counter, delay):
	if delay >= 5:
		raise Exception("Delay can not be more than that")
	while counter:
		time.sleep(delay)
		print "%s: %s" % (threadName, time.ctime(time.time()) )
		counter -= 1

# # Create new threads
# t1 = MyThread(1, "Thread-1", 3, 4)
# t2 = MyThread(2, "Thread-2", 4, 2)

# # start new threads
# print t1.start()
# print t2.start()



# class MyThread(threading.Thread):
# 	def __init__(self, threadID, name, counter):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter

# 	def run(self):
# 		print "Staring" , self.name
# 		threadLock.acquire()
# 		print_time( self.name, self.counter, 2)
# 		threadLock.release()


# threadLock = threading.Lock()
# threads = []

# # Create new threads
# t1 = MyThread(1, "Thread-1", 3)
# t2 = MyThread(2, "Thread-2", 4)

# # start new threads
# print t1.start()
# print t2.start()

# threads.append(t1)
# threads.append(t2)

# for i in threads:
# 	i.join()

# print "Exiting main thread"


# # Threading with Queue
# import Queue
# import threading
# import time

# exitFlag = 0

# class MyThread(threading.Thread):
# 	def __init__(self, threadID, name, q):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.q = q
	
# 	def run(self):
# 		print "Staring:", self.name
# 		process_data(self.name, self.q)
# 		print "Exiting:", self.name

# def process_data(threadName, q):
# 	print "precs data"
# 	while not exitFlag:
# 		queueLock.acquire()
# 		print "while"
# 		if not workQueue.empty():
# 			print "if not"
# 			data = q.get()
# 			queueLock.release()
# 			print "%s processing %s" % (threadName, data)
# 		else:
# 			print "else"
# 			queueLock.release()
# 		time.sleep(1)

# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]

# queueLock = threading.Lock()
# workQueue = Queue.Queue(10)
# threads = []
# threadID = 1

# for tName in threadList:
# 	thread = MyThread(threadID, tName, workQueue)
# 	thread.start()
# 	threads.append(thread)
# 	threadID += 1
# 	print "for"

# queueLock.acquire()
# for word in nameList:
# 	workQueue.put(word)
# queueLock.release()

# while not workQueue.empty():
# 	pass

# exitFlag = 1

# for t in threads:
# 	t.join()

# print "Exiting Main thread"



# ===================

# class B(object):
# 	def __init__(self, id):
# 		self.id = id
# 	def num(self):
# 		pass
# 	# def __str__(self):
# 	# 	return "This is Object b"
# 	def __repr__(self):
# 		b = "B("+str(self.id)+ ")"
# 		return b





# b = B(100)
# print type( repr(b) )

# b.__dict__['age'] = 49
# print dir(b)
# print b.__dict__
# print b.age + len(b.__dict__)

# print b
# print str(b)
# print eval( repr(b) )
# print b == str(b)
# print b == eval(repr(b))

# c = B(100)
# print c == eval(repr(c))

# print 9/1.6

# print 2**8
# print 2**16
# print 16**3*15 + 16**2*15 + 16**1*15 + 15


# ====================================

# class A(object):
# 	def __init__(self):
# 		self.__priv = 3
# 		self._prot = 4


# a = A()
# print dir(a)
# print a._prot


# ====================================

# class A(object):
# 	clv = 3
# 	def __init__(self):
# 		pass

# 	@staticmethod
# 	def st():
# 		print "st"

# 	@classmethod
# 	def cl(cls):
# 		print "cl"
# 		print cls

# 	def hi(self):
# 		print "hi"


# a = A()
# b = A()
# print A.hi()

# m = a.hi
# print dir(a.hi)
# print dir(a.st)
# print dir(a.cl)

# print a.st("sa")
# print A.st()
# print A.cl()
# print a.cl()

# print a.clv
# a.clv = 4
# print b.clv
# A.clv = 35
# print a.clv
# print b.clv

# import abc
# print dir(abc)


# ====================================

# class C(object):
# 	@staticmethod
# 	def st():
# 		print "C hi"

# 	@classmethod
# 	def cl(cls):
# 		print "C cl"

# c = C()
# c.st()
# c.cl()
# C.st()
# C.cl()

# ====================================


# import abc

# class A(object):

# 	__metaclass__ = abc.ABCMeta
# 	def __init__(self):
# 		print "init A"

# 	# Since you have defined, metaclass = ABCMeta
# 	# and declared this as abstractmethod,
# 	# all the sub classes of this class will have to implement this Abstract method
# 	@classmethod
# 	@abc.abstractmethod
# 	def hi(self):
# 		return "hi A"

# class B(A):

# 	def __init__(self):
# 		print "init B"

# 	# Now, this will have to be implemented, otherwise, we will have an error
# 	@staticmethod
# 	def hi():
# 		print "hi B"

# b = B()
# print b.hi()


# ====================================

# class Meta(type):
# 	def __new__(meta, name, bases, dct):
# 		# print "meta new"
# 		return super(Meta, meta).__new__(meta, name, bases, dct)

# 	# def __init__(cls, name, bases, dct):
# 	# 	print "meta init"

# 	# def __call__(cls):
# 	# 	print "meta call"

# 	pass

# class A(object):
# 	__metaclass__ = Meta
# 	def __call__(self):
# 		# return "call"
# 		pass

# class B(A):

# 	def __init__(self):
# 		print B

# # print type(A)
# a = A()

# b = B()
# print b.__metaclass__
# print dir(b)

# # print type(object)
# # print type(A)
# # print type(a)



# ====================================


# class B(object):
# 	b = 1

# from abc import *

# class Customer(object):
# 	# __metaclass__ = ABCMeta
	
# 	c = 2
# 	def __init__(self, name, balance):
# 		self.name = name
# 		self.balance = balance

# 	def withdraw(self, amount):
# 		if amount > self.balance:
# 			raise RuntimeError("Amount greated than available balance.")
# 		self.balance -= amount
# 		return self.balance

# 	def deposit(self, amount):
# 		self.balance += amount
# 		return self.balance

# 	def a(self):
# 		print "Aa"

# 	# @abstractmethod
# 	def ab(self):
# 		print "ab"

	

# c = Customer('a', 1)
# cc = Customer('b', 2)


# c.ab()





# ====================================











