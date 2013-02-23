# This python script generate a file named readme.txt 
# into each car folder.

# It use the file carDb.cvs (located in this same directory) as a source for the data
# this cvs file has all fields quoted with ["] a separated by a [,]
# and can be easily opened and edited with LibreOffice Spreadshit or similar

import os
import sys
import csv

titles='';

with open('carDb.csv', 'rb') as csvfile:
	fileRows = csv.reader(csvfile, delimiter=',', quotechar='"')

	#skip the first line of the cvs file
	next(fileRows)

	#for the others lines generate the readme
	for row in fileRows:

		#get data
		carAutor = '* '+row[0].replace("\n", "\n* "); #do a list
		carLicence =  row[1]
		carName =  row[2]
		carCategory =  row[3]
		carFolder =  row[4]

		#url of the readme
		readmeFileUrl = './../cars/'+carFolder+'/readme.txt'

		#generare content of the readme
		readmeContent="## Autor(S) ##\n\n"+carAutor;
		readmeContent+="\n\n## Licence ##\n\n"+carLicence;
		readmeContent+="\n\n## Car name ##\n\n"+carName;
		readmeContent+="\n\n## Car Category ##\n\n"+carCategory;
		readmeContent+="\n\n## Car Folder ##\n\n"+carFolder;
		
		#save into the file
		readmeFile = open(readmeFileUrl,"w")
		readmeFile.write(readmeContent)
		readmeFile.close()

