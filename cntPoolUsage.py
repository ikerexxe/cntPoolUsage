#!/usr/bin/python
'''
 ' cntPoolUsage.py
 ' Author: Iker Pedrosa
 ' 
 ' License:
 ' This file is part of cntPoolUsage.
 ' 
 ' cntPoolUsage is free software: you can redistribute it and/or modify
 ' it under the terms of the GNU General Public License as published by
 ' the Free Software Foundation, either version 3 of the License, or
 ' (at your option) any later version.
 ' 
 ' cntPoolUsage is distributed in the hope that it will be useful,
 ' but WITHOUT ANY WARRANTY; without even the implied warranty of
 ' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 ' GNU General Public License for more details.
 ' 
 ' You should have received a copy of the GNU General Public License
 ' along with cntPoolUsage.  If not, see <http://www.gnu.org/licenses/>.
 ' 
'''

#Imported modules
import urllib2
import re

#Global variables
pageToDownload = ""

def getPageName():
	global pageToDownload
	intermediateWeb = "http://clubnatacioterrassa.cat/el-club/installacions/"
	
	response = urllib2.urlopen(intermediateWeb)
	searchText = re.compile("http://clubnatacioterrassa.cat/wp-content/uploads/(.*?)/(.*?)/Disponibilitat_piscines_(.*?).pdf")
	tmp = searchText.search(response.read())
	pageToDownload = tmp.group(0)
	response.close()

	print("Location of pool usage file: %s" % pageToDownload)
#Finished getPageName

def downloadFile():
	global pageToDownload
	documentName = "Disponibilitat_piscines.pdf"
	
	response = urllib2.urlopen(pageToDownload)
	file = open(documentName, 'wb')
	file.write(response.read())
	file.close()
	response.close()
	print("Pool usage document downloaded")
#Finished downloadFile

def main():
	getPageName()
	downloadFile()
#Finished main

if __name__ == "__main__":
    main()
