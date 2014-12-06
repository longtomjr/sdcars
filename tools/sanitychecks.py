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
import re
currentDir = '';

#
#
#
def check( xmlEntity ):
	"check if a given string is lowercase if not make it lowercase"
	#fix to lowercase
	for result in root.findall(xmlEntity):
		if result.attrib['val'] != str.lower(result.attrib['val']):
			print "Fixing "+result.attrib['val'];
			result.attrib['val'] = str.lower(result.attrib['val']);
			print "Fixed!";

		#check for file existence
		if not os.path.isfile(currentDir+result.attrib['val']):
			print 'Unable to find file: '+currentDir+result.attrib['val']

		#if the file is an ac or acc file
		#check for textures files used existence
		#file = re.findall('texture".*"', 'texture "carf10-trb1.png" base')
		fileName, fileExtension = os.path.splitext(currentDir+result.attrib['val'])
		#print fileName+fileExtension;
		if fileExtension == '.ac' or fileExtension == '.acc':
			print "Checking textures for "+fileName+fileExtension;

			with open (fileName+fileExtension, "w+b") as myfile:
				text=myfile.read()
				for m in re.finditer(r"(?<=texture \")(.*)(?=\")", text):
					textureFileUrl = currentDir+m.group(0);
					textureFileUrlLowercase = textureFileUrl.lower();
					if textureFileUrl != textureFileUrlLowercase:
						print "=== replaced ==="
						text.replace(textureFileUrl, textureFileUrlLowercase)
						myfile.write(text);
					if not os.path.isfile(textureFileUrl):
						print 'Unable to find file: '+m.group(0)
					
	return 




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
	global currentDir;
	currentDir = newDirName;
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

	#sound file
#	check("./section[@name='Sound']/attstr[@name='engine sample']");

	#wheel texture file
#	check("./section[@name='Graphic Objects']/attstr[@name='wheel texture']");

	#shadow texture file
	check("./section[@name='Graphic Objects']/attstr[@name='shadow texture']");

	#speedometer texture file
#	check("./section[@name='Graphic Objects']/attstr[@name='speedometer texture']");

	#car acc file
	check("./section[@name='Graphic Objects']/section[@name='Ranges']/section[@name='1']/attstr[@name='car']");

	#wheel acc file
	check("./section[@name='Graphic Objects']/section[@name='Steer Wheel']/attstr[@name='model']");

	#hi res wheel acc file
	check("./section[@name='Graphic Objects']/section[@name='Steer Wheel']/attstr[@name='hi res model']");

	#driver files
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='1']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='2']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='3']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='4']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='5']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='6']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='7']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='8']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='9']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='10']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='11']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='12']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='13']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='14']/attstr[@name='driver']");
	check("./section[@name='Graphic Objects']/section[@name='Driver']/section[@name='15']/attstr[@name='driver']");


	#car category
	for category in root.findall("./section[@name='Car']/attstr[@name='category']"):
		carCategory=category.attrib['val']
		#if category.attrib['val'] != str.lower(category.attrib['val']):
		#	print "Fixing "+category.attrib['val'];
	if not categoryNames.has_key(carCategory):
		print "INVALID category -"+ carCategory +"- for car "+newDirName;

	#save the modified xml file
	tree.write(xmlFileUrl)

