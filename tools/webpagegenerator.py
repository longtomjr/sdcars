# this python script generate an html page
# with all the cars and theyr prewievs

import os
import sys
import shutil
import xml.etree.ElementTree as ET


#=====================
#get a list of the folders in the cars directory
carFolders =  os.listdir('./../cars/')

carCount = 0;

tmpout={};

for folder in carFolders:
	dirName='./../cars/'+folder+'/'

	xmlFileUrl=dirName+folder+'.xml'

	tree = ET.parse(xmlFileUrl)

	#
	carCount=carCount+1;

	#and get the root of the xml tree
	root = tree.getroot()

	#car name
	carName=root.attrib['name']

	#car prewiew
	carImg = './cars/'+folder+'/'+folder+"-preview.jpg"
	print carName +"("+folder+")";

	#generate info table of the car
	category= root.findall("./section[@name='Car']/attstr[@name='category']")[0].attrib['val']

	#insert the info table inside a category based array
	if tmpout.has_key(category):
		tmpout[category]+='';
	else:
		tmpout[category]='';

	tmpout[category]+= "\n<tr>"
	tmpout[category]+= "<td><img width='300px' src='"+carImg+"'></td>"
	tmpout[category]+= "<td>"
	tmpout[category]+= "Name: <b>"+carName+"</b>"
	tmpout[category]+= "<br>Category: "+root.findall("./section[@name='Car']/attstr[@name='category']")[0].attrib['val']
	if len(root.findall("./section[@name='Drivetrain']/attstr[@name='type']")): 
		tmpout[category]+= "<br>Drivetrain: "+root.findall("./section[@name='Drivetrain']/attstr[@name='type']")[0].attrib['val']
	tmpout[category]+= "<br>Weight: "+	root.findall("./section[@name='Car']/attnum[@name='mass']")[0].attrib['val'] +" "+ root.findall("./section[@name='Car']/attnum[@name='mass']")[0].attrib['unit']
	tmpout[category]+= "<br>Engine: "
	if len(root.findall("./section[@name='Engine']/attnum[@name='cylinders']")):
		tmpout[category]+= "<br>Cilinders: "+root.findall("./section[@name='Engine']/attnum[@name='cylinders']")[0].attrib['val']
		tmpout[category]+= "<br>Capacity: "+root.findall("./section[@name='Engine']/attnum[@name='capacity']")[0].attrib['val']
		#out+= "<br>Capacity: "+root.findall("./section[@name='Engine']/attnum[@name='capacity']")[0].attrib['val'] +" "+ root.findall("./section[@name='Car']/attnum[@name='capacity']")[0].attrib['unit']
	tmpout[category]+= "</td>"
	tmpout[category]+= "</tr>"

# create a table
out= '''
<!doctype html>
<html class="no-js" lang="">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Speed Dreams Unofficial/Usermade Cars</title>
<meta name="description" content="">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
'''
out+="<b>"+str(carCount)+"</b>cars available!";
out+='<table>';

# insert the table content
for category in tmpout:
	out+=tmpout[category];
out+= '''
</table>
</body>
</html>
'''

#save all into a file
out_file = open("./../index.html","w")
out_file.write(out)
out_file.close()
