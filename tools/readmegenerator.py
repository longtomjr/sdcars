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
	carImg = '/cars/'+folder+'/'+folder+"-preview.jpg"
	print carName +"("+folder+")";

	#generate info table of the car
	category= root.findall("./section[@name='Car']/attstr[@name='category']")[0].attrib['val']

	#insert the info table inside a category based array
	if tmpout.has_key(category):
		tmpout[category]+='';
	else:
		tmpout[category]='';

	#tmpout[category]+= "\n!["+carName+"](/../master"+carImg+'?raw=true =150x"'+carName+'")'
	tmpout[category]+= '<img src="/../master'+carImg+'" width="200px" alt="'+carName+'">'

# create a table
out= '''
sdcars
======

Unnoficial (usermade) Speed Dreams cars

This package contains car-mods for the open source racing game [Speed Dreams](http://www.speed-dreams.org)

We corrently count **''' 

out+= str(carCount);

out+= '''** playable cars in this package.

[Download it now!](https://github.com/longtomjr/sdcars/archive/master.zip)


Included cars mod previews
======

'''
# insert PREVIEWS
for category in tmpout:
	out+=tmpout[category];

# coontact informations
out+= '''


Contact informations
======

If you wanto to add you mod to this repo, or for any info about it feel free to contact us!

Longtomjr - longtomjr [at] gmail.com

Madbad - madbad82 [at] gmail.com
'''


#save all into a file
out_file = open("./../README.md","w")
out_file.write(out)
out_file.close()
