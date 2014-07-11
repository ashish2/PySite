#!/usr/bin/env python

__author__='ashish'

import csv
import sys
import os
from collections import *

companies = OrderedDict()
separator = ';'

def read_csv(csv_file):
	"""Read a passed csv file"""
	fobj = open(csv_file, "rb")
	first_line = fobj.readline().strip()
	
	for i in first_line.split(separator)[2:]:
		companies[i] = [[], [], []]
		
	for line in fobj:
		yield line
	

def loop(csv_file):
	y = 0
	for i in read_csv(csv_file):
		lis = i.strip().split(separator)
		z = 0
		for comp_name, val in companies.items():
			val[0].append( int( lis[0] ) )
			val[1].append( lis[1] )
			val[2].append( int( lis[z+2] ) )
			z = z+1
	
	string = ''
	for comp_name, val in companies.items():
		"""Max out"""
		mx = max(val[2])
		indx = val[2].index(mx)
		g0 = val[0][indx]
		g1 = val[1][indx]
		
		companies[comp_name] = zip( [g0], [g1], [mx] )
		string += str(comp_name) + ": " + str(g0) + " " + g1 + ", " + str(mx) + '\n'
	
	return string
	"""return companies"""

def format_csv(companies):
	pass

def print_results(companies):
	
	print "companies"
	print companies.__str__()
	


def run_procedure(csv_file):
	#genobj = read_csv(csv_file)
	result = loop( csv_file)
	print_results(result)
	


if __name__ == "__main__":
	"""Takes in a csv filename from command line & starts the procedure
	cd into this directory & run python read_csv.py 'test_shares_data.csv'
	"""
	try:
		if len(sys.argv) == 2:
			try:
				csv_file = sys.argv[1]
				is_file = os.path.isfile(csv_file)
				if is_file: 
					run_procedure(csv_file)
			except:
				raise Exception("Not a valid file")
	except:
		raise Exception("No file given")
	
