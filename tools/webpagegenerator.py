# this python script generate an html page
# with all the cars and theyr prewievs

import os
import sys
import shutil
import xml.etree.ElementTree as ET


#=====================
#get a list of the folders in the cars directory
carFolders =  os.listdir('./../cars/')

out=""
out+= "<table>"

for folder in carFolders:

	dirName='./../cars/'+folder+'/'

	xmlFileUrl=dirName+folder+'.xml'

	tree = ET.parse(xmlFileUrl)

	#and get the root of the xml tree
	root = tree.getroot()

	#car name
	carName=root.attrib['name']

	#car prewiew
	carImg = './cars/'+folder+'/'+folder+"-preview.jpg"
	print carName +"("+folder+")";
	#generate info table of the car
	out+= "<tr>"
	out+= "<td><img width='300px' src='"+carImg+"'></td>"
	out+= "<td>"
	out+= "<br>Name: <b>"+carName+"</b>"
	out+= "<br>Category: "+root.findall("./section[@name='Car']/attstr[@name='category']")[0].attrib['val']
	out+= "<br>Drivetrain: "+root.findall("./section[@name='Drivetrain']/attstr[@name='type']")[0].attrib['val']
	out+= "<br>Weight: "+	root.findall("./section[@name='Car']/attnum[@name='mass']")[0].attrib['val'] +" "+ root.findall("./section[@name='Car']/attnum[@name='mass']")[0].attrib['unit']
	out+= "<br>Engine: "
	#out+= "<br>Cilinders: "+root.findall("./section[@name='Engine']/attstr[@name='cylinders']")[0].attrib['val']
	#out+= "<br>Capacity: "+root.findall("./section[@name='Engine']/attstr[@name='cylinders']")[0].attrib['val'] +" "+ root.findall("./section[@name='Car']/attnum[@name='mass']")[0].attrib['unit']
	out+= "</td>"
	out+= "</tr>"


out+= "</table>"

#save into a file
out_file = open("./../index.html","w")
out_file.write(out)
out_file.close()
