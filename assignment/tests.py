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
import read_csv as rc

class SimpleTest(unittest.TestCase):
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		self.assertEqual(1 + 1, 2)
		

class OurCsvTest(unittest.TestCase):
	"""
	Test Cases for the functions in our read_csv.py
	"""
	
	def __init__(self, testname, csv_file):
		super(OurCsvTest, self).__init__(testname)
		self.csv_file = csv_file
		
	
	def test_pass(self):
		self.assertTrue(True)
	
	def test_read_csv_type(self):
		"""
		Tests return type: 
		Tests that our read_csv function returns a 
		generator object after taking in a file
		"""
		gen = rc.read_csv( self.csv_file )
		self.assertIsInstance( gen, type( ( i for i in range(1) ) ) )
	

if __name__ == '__main__':
	"""Takes in a csv filename from command line & starts the procedure
	cd into this directory & run python read_csv.py 'test_shares_data.csv'
	"""
	
	logging.basicConfig( stream=sys.stderr )
	logging.getLogger( "OurCsvTest" ).setLevel( logging.DEBUG )
	log= logging.getLogger( "OurCsvTest" )
	
	try:
		if len(sys.argv) == 2:
			try:
				csv_file = sys.argv[1]
				is_file = os.path.isfile(csv_file)
			except:
				raise Exception("Not a valid file")
	except:
		raise Exception("No file given")
	
	
	#unittest.main()
	suite = unittest.TestSuite()
	suite.addTest(OurCsvTest("test_read_csv_type", csv_file ))
	unittest.TextTestRunner().run(suite)
		
