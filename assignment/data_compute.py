''' data_compute.py

This program calculates year, month in which the share price was highest for each company
provided in the csv file
'''

import csv
import sys

def compute_company_data(file_name) :
	'''computes year, month in which the share price was highest for each company

	input
	file_name : string containing input file name

	output:
	output_list : list containg lists with comapny name,year, month, heighest share value
	
	'''

	z = 0
	output_list =[]

	try :
		
		with open(file_name, 'rb') as csvfile:
			##list of company names
			companies = csvfile.readline().rstrip().split(';')[2:]
	  
			g = globals()
			#Creating dynamic list for each comapny which will store the highest value
			for i in range(len(companies)):
				g['list_{0}'.format(i)] = [companies[i],0,0,0]
			
			#reading the first line
			line = list(csvfile.readline().rstrip().split(';'))
			
			while len(line) > 1 and line:
				#Calculating the highest value for each company
				for i in range(len(companies)):
					if int(g['list_{0}'.format(i)][3]) < int(line[i+2]) :
						g['list_{0}'.format(i)]= [companies[i],line[0],line[1],line[i+2]]
			  
				#incrementing the line 
				line = list(csvfile.readline().rstrip().split(';'))
			  
			for i in range(len(companies)):
				output_list.append(g['list_{0}'.format(i)])
	except:
		raise Exception("invalid data")
			
	print "output in form of list [ Comapany Nmae, year, Month, Share Price]: \n"  + repr(output_list)
	return output_list

if __name__ == '__main__':

	#takes file name as command line argument
	if len(sys.argv) > 1 :
		file_name = sys.argv[1]
	else :
		#file_name = 'input_data.csv' 
		file_name = 'test_shares_data_2.csv'

	compute_company_data(file_name)


		
	
