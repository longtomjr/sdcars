# this python script generate (at the base of this repository) the README.md file
# displayed by github

import os
import sys
#import shutil
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

	#get the category of the car from its xml file
	category= root.findall("./section[@name='Car']/attstr[@name='category']")[0].attrib['val']

	#group cars data by category
	if tmpout.has_key(category):
		tmpout[category]+='';
	else:
		tmpout[category]='';

	#generate the img tag for the preview
	tmpout[category]+= '<img src="/../master'+carImg+'" width="200px" alt="'+carName+'">'


# generate the README.md content
out= '''
Speed Dreams Cars
======

Unoficial (usermade) Speed Dreams car-mods.

This package contains car-mods for the open source racing game [Speed Dreams](http://www.speed-dreams.org)

We currently count **''' 

out+= str(carCount);

out+= '''** playable cars in this package.

**[Download it now!](https://github.com/longtomjr/sdcars/archive/master.zip)**


Included car-mods previews
======

'''
# insert previously generated previews
for category in tmpout:
	out+=tmpout[category];

# add contact informations
out+= '''


Contact informations
======

If you want to add your mod to this repo, or for any info about it feel free to contact us!

Longtomjr - longtomjr [at] gmail.com

Madbad - madbad82 [at] gmail.com
'''


#save all into the file
out_file = open("./../README.md","w")
out_file.write(out)
out_file.close()
