import sys
import zipfile



filename = sys.argv[1]

def isZip (filename) :
	with zipfile.ZipFile(filename) as zf: 
		xmlCode = zf.open("word/document.xml").read().decode("utf8")
		docContents = ""
		while (len(xmlCode) > 0) :
			xmlCode = xmlCode.partition('<w:t>')
			if (xmlCode[2] == "") :
				break;
			xmlCode = xmlCode[2].partition("</w:t>")
			docContents += xmlCode[0]
			xmlCode = xmlCode[2]
	return docContents

if (filename.rfind(".docx") + 5 == len (filename)) :
	s = isZip(filename)
elif (filename.rfind(".txt") + 4 == len (filename)) :
	f = open (sys.argv[1], 'r')
	s = f.read()
else :
	print ("Not a .docx or .txt file")

count = 0
for c in s :
	if ord(c) > 0x4E00 and ord(c) < 0x9FFF:
		count += 1
print (count)

