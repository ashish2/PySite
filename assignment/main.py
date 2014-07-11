#!/usr/bin/env python

__author__='ashish'

import os
import sys
from read_csv import *
import tests

csv_file = 'test_shares_data_2.csv'

if __name__ == "__main__":
	"""Takes in a csv filename from command line & starts the procedure"""
	print sys.argv
	if sys.argv == 1:
		if is_csvfile:
			sys.argv
		except:
			NotACsvFile
	except:
		NoFileGiven
		
		
	
if __name__ == '__main__':
	csv_file = 'test_shares_data.csv'
	run_procedure(csv_file)
	
