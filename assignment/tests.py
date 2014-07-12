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
from read_csv import ComputeData


class OurCsvTest(unittest.TestCase):
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
		
	

if __name__ == '__main__':
	unittest.main()
	
