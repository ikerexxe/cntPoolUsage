#Imported modules
import urllib2
import re

#Global variables
pageToDownload = ""

def getPageName():
	global pageToDownload
	intermediateWeb = "http://www.clubnatacioterrassa.cat/inici/instal%C2%B7lacions-area-olimpica/piscines/"
	
	response = urllib2.urlopen(intermediateWeb)
	searchText = re.compile("http://www.clubnatacioterrassa.cat/wp-content/uploads/Disponibilitat_piscines_(.*?).pdf")
	tmp = searchText.search(response.read())
	pageToDownload = tmp.group(0)

	print("Location of pool usage file: %s" % pageToDownload)
#Finished getPageName

def downloadFile():
	global pageToDownload
	documentName = "Disponibilitat_piscines.pdf"
	
	response = urllib2.urlopen(pageToDownload)
	file = open(documentName, 'wb')
	file.write(response.read())
	file.close()
	print("Pool usage document downloaded")
#Finished downloadFile

def main():
	getPageName()
	downloadFile()
#Finished main

if __name__ == "__main__":
    main()