from zipfile import ZipFile

def unpack(pwd):
	try:
		with ZipFile("geschenk.zip") as pack:
			pack.extractall(pwd=pwd.encode("utf8"))
		return(True)
	except:
		return(False)
	
def get_rock():
	with open("rockyou.txt", 'r', encoding="latin-1", errors="ignore") as f:
		rock = f.read().splitlines()
	return(rock)

def main():
	rock = get_rock()
	for passwd in rock:
		if len(passwd) == 96: #4*24
			if unpack(passwd):
				print("Passoword is:[ {} ]!".format(passwd))
	
if __name__ == "__main__":
	main()