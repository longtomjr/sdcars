# this python script rename all folders and file names to be lowercase
# need to chech if xml and ac / acc files need tweak to use lowercase filenames too

# need to check in .xml file 
#							(done)	Sound->engine sample
#							(done)	Graphic Objects->wheel texture
#							(done)	Graphic Objects->shadow texture
#							(done)	Graphic Objects->speedometer texture
# 							(done:but no correction applied)	car->category
#							(done) car ac/acc file

#in ac/acc
#texture "filename"

import os
import sys
import shutil
import xml.etree.ElementTree as ET

#=====================
# get a list of available categories
#=====================

print "=================================="
print "Checking sanity of category files:"
print "=================================="
categoryNames={};
categoriesFiles =  os.listdir('./../categories/')
for file in categoriesFiles:
	
	#rename the file

	tree = ET.parse('./../categories/'+file)

	#and get the root of the xml tree
	root = tree.getroot()

	categoryName = root.findall("./section[@name='Car']/attstr[@name='category']")[0].attrib['val']
	categoryNames[categoryName]=''
	if categoryName+".xml" == file:
		print "ok: "+file
	else:
		print file+" wrong "+categoryName
		print "Renaming category file "+file+" to "+categoryName+".xml";
		os.rename('./../categories/'+file, './../categories/'+categoryName+".xml")
		print "Done!"
#=====================
# folder renaming
#=====================
print "=================================="
print "Checking sanity of car files:"
print "=================================="
#get a list of the folders in the cars directory
carFolders =  os.listdir('./../cars/')

for folder in carFolders:

	#get current folder name
	oldDirName='./../cars/'+folder+'/'

	#transform it to lower case
	newDirName='./../cars/'+str.lower(folder)+'/'

	#if currentname is not lowercase then rename the folder to lowercase
	if oldDirName != newDirName:
		print "Need to rename dir: "+oldDirName

		#rename the folder
		shutil.move(oldDirName, newDirName)
#=====================
# file renaming
#=====================
	# get a list of the files of the current folder
	folderFiles = os.listdir(newDirName)
	
	for file in folderFiles:
		#get current folder name
		oldFileName=file

		#transform it to lower case
		newFileName=str.lower(file)
	
		if oldFileName != newFileName:
			print "Need to rename file: "+oldFileName+" from "+newDirName

			oldFileUrl = newDirName+oldFileName
			newFileUrl = newDirName+newFileName

			#rename the file
			os.rename(oldFileUrl, newFileUrl)

	#=====================
	# file content fixing (xml file)
	#=====================
	#read the xml file of the car
	xmlFileUrl=newDirName+str.lower(folder)+'.xml'
	tree = ET.parse(xmlFileUrl)

	#and get the root of the xml tree
	root = tree.getroot()

	#log the car name
	carName=root.attrib['name']

	#sound
	for category in root.findall("./section[@name='Sound']/attstr[@name='engine sample']"):
		carSoundFile=category.attrib['val']


	#wheel texture
	for category in root.findall("./section[@name='Graphic Objects']/attstr[@name='wheel texture']"):
		carWheelTexture=category.attrib['val']
		if category.attrib['val'] != str.lower(category.attrib['val']):
			print "Fixing "+category.attrib['val'];

	#shadow texture
	for category in root.findall("./section[@name='Graphic Objects']/attstr[@name='shadow texture']"):
		carShadowTexture=category.attrib['val']
		if category.attrib['val'] != str.lower(category.attrib['val']):
			print "Fixing "+category.attrib['val'];

	#speedometer texture
	for category in root.findall("./section[@name='Graphic Objects']/attstr[@name='speedometer texture']"):
		carSpeedometerTexture=category.attrib['val']
		if category.attrib['val'] != str.lower(category.attrib['val']):
			print "Fixing "+category.attrib['val'];

	#car acc filename
	for category in root.findall("./section[@name='Graphic Objects']/section[@name='Ranges']/section[@name='1']/attstr[@name='car']"):
		carFile=category.attrib['val']
		if category.attrib['val'] != str.lower(category.attrib['val']):
			print "Fixing "+category.attrib['val'];
			category.attrib['val'] = str.lower(category.attrib['val']);
			print "Fixed!";

	#car category
	for category in root.findall("./section[@name='Car']/attstr[@name='category']"):
		carCategory=category.attrib['val']
		#if category.attrib['val'] != str.lower(category.attrib['val']):
		#	print "Fixing "+category.attrib['val'];
	if not categoryNames.has_key(carCategory):
#		print "valid category"
#	else:
		print "INVALID category -"+ carCategory +"- for car "+newDirName;

	#save the modified xml file
	tree.write(xmlFileUrl)
'''
	print "======= "+carName+" ======="
	print xmlFileUrl
	print carFile
	print carSoundFile
	print carWheelTexture
	print carShadowTexture
	print carSpeedometerTexture
	print carCategory+"\n\n"
'''
