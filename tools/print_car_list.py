# this python script generate a file named car_list.txt at the base of this repository
# with a list of all the cars present into the cars folder


import os
import sys
import xml.etree.ElementTree as ET


out="List of available cars:\n"

#get a list of the folders in the cars directory
carFolders =  os.listdir('./../cars/')

for folder in carFolders:
	#read the xml file of the car
	xmlFileUrl='./../cars/'+folder+'/'+folder+'.xml'
	tree = ET.parse(xmlFileUrl)

	#and get the root of the xml tree
	root = tree.getroot()
	root.findall(".")

	#log the car name
	out+="\n- "+root.attrib['name']

	#log the folder name
	out+=' (from folder: "'+folder+'")'


#save into a file
out_file = open("./../car_list.txt","w")
out_file.write(out)
out_file.close()
