#!/usr/bin/env python

__author__='ashish'

import csv
import sys
import os
from collections import *

separator = ';'

def read_csv(csv_file, companies):
	"""Read a passed csv file as a Generator object"""
	fobj = open(csv_file, "rb")
	first_line = fobj.readline().strip()
	for i in first_line.split(separator)[2:]:
		companies[i] = [ 0, 0, 0 ]
	for line in fobj:
		yield line
	
def loop(csv_file, companies):
	"""Loops over a generator object & fills an OrderedDict of companies"""
	y = 0
	for i in read_csv(csv_file, companies):
		lis = i.strip().split(separator)
		z = 0
		for comp_name, val in companies.items():
			numb = z+2
			if val[2] < int( lis[numb] ):
				( val[0], val[1], val[2] ) = ( int( lis[0] ) , lis[1], int( lis[numb] ) )
			z = z+1
	
	return companies

def format_csv(companies):
	"""Formats a Dict into a string to make it printable"""
	string =  ''.join([str(comp_name)+": "+ ', '.join(map(str, val))+'\n' for comp_name, val in companies.items()])
	return string

def print_results(companies):
	
	print "companies"
	print companies.__str__()
	


def run_procedure(csv_file):
	companies = OrderedDict()
	
	#genobj = read_csv(csv_file)
	ret_companies = loop(csv_file, companies)
	result = format_csv(ret_companies)
	print_results(result)
	


if __name__ == "__main__":
	"""Takes in a csv filename from command line & starts the procedure
	cd into this directory & run python read_csv.py 'test_shares_data.csv'
	"""
	
	#compute
	#run_tests
	
	#try:
	if len(sys.argv) == 2:
		#try:
			csv_file = sys.argv[1]
			is_file = os.path.isfile(csv_file)
			if is_file: 
				run_procedure(csv_file)
		#except:
			#raise Exception("Not a valid file")
	#except:
		#raise Exception("No file given")
	
