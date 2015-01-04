
"""

class MetaSingleton(type):
	instance = None
	def __call__(cls, *args, **kw):
		if cls.instance is None:
			cls.instance = super(MetaSingleton, cls).__call__(*args, **kw)
		return cls.instance

class Foo(object):
	__metaclass__ = MetaSingleton
	c = 1


a = Foo()
b = Foo()
# assert a is b
print dir(a)
print dir(b)

print a.c
print b.c
a.c = 2
print a.c
print b.c

"""


# ===============================================

"""

a- 	b -	
|\/	| -_  e
c -	d -

"""


def fac(n):
	if n > 0:
		return n + fac(n-1)
	else:
		return 0





# ===============================================


def make_hook(f):
	"""Decorator to turn 'foo' method into '__foo__'"""
	f.is_hook = 1
	return f

class MyType(type):
	def __new__(cls, name, bases, attrs):

		if name.startswith('None'):
			return None

		# Go over attributes and see if they should be renamed.
		newattrs = {}
		for attrname, attrvalue in attrs.iteritems():
			if getattr(attrvalue, 'is_hook', 0):
				newattrs['__%s__' % attrname] = attrvalue
			else:
			   newattrs[attrname] = attrvalue

		return super(MyType, cls).__new__(cls, name, bases, newattrs)

	def __init__(self, name, bases, attrs):
		super(MyType, self).__init__(name, bases, attrs)

		# classregistry.register(self, self.interfaces)
		print "Would register class %s now." % self

	def __add__(self, other):
		class AutoClass(self, other):
			pass
		return AutoClass
		# Alternatively, to autogenerate the classname as well as the class:
		# return type(self.__name__ + other.__name__, (self, other), {})

	def unregister(self):
		# classregistry.unregister(self)
		print "Would unregister class %s now." % self

class MyObject:
	__metaclass__ = MyType
	pass

class NoneSample(MyObject):
	pass

# Will print "NoneType None"
print type(NoneSample), repr(NoneSample)

class Example(MyObject):
	def __init__(self, value):
		self.value = value
	@make_hook
	def add(self, other):
		return self.__class__(self.value + other.value)

# Will unregister the class
# Example.unregister()

inst = Example(10)
# print inst

print "inst + inst"

# Will fail with an AttributeError
# inst.unregister()


print inst + inst

class Sibling(MyObject):
	pass

ExampleSibling = Example + Sibling
# ExampleSibling is now a subclass of both Example and Sibling (with no
# content of its own) although it will believe it's called 'AutoClass'
print ExampleSibling
print ExampleSibling.__mro__


# ======================================




