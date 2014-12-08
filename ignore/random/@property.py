#!/usr/bin/env python

class A(object):

	def __init__(self):
		self._x = 3
		pass

	def foo():
	    doc = "The foo property."
	    def fget(self):
	        return self._foo
	    def fset(self, value):
	        self._foo = value
	    def fdel(self):
	        del self._foo

	    loc = locals()
	    print loc
	    return loc
	foo = property(**foo())

	@property
	def x(self):
		return self._x
	@x.setter
	def x(self, val):
		self._x = val
	@x.deleter
	def x(self):
		del self._x

a = A()

print dir(a)
print a.x
a.x = 2
print a.x

print ""

a.foo = 5
print a.foo


# ===============================================


# print **foo()


def c(*li, **di):
	print "li"
	print li
	print "di"
	print di

li= [4,5,6]
di = {"a":1, "b":2, "c": 3}

c(*li, **di)



# ===============================================






