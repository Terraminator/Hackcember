from zipfile import ZipFile
import os

   
def unpack(name):
	with ZipFile(str(name), 'r') as zipObj:
	   zipObj.extractall()
	os.system("del " + name)
	   
def get_zip():
	files = os.listdir()
	for file in files:
		if ".zip" in file:
			unpack(file)
	
	if len(files) < 1:
		return(False)
	else:
		return(True)
	
while get_zip():
	pass