import binascii

def get_text(path):
	with open(str(path), "r") as msg:
		text = msg.read().lower()
	return(text)
	
def byte_to_int(byte):
	return(int(byte, 2))
	
def decode(bin):
	dec = ""
	byte = ""
	ints = []
	w = 0
	print(bin)
	for i in range(1, len(bin)+1):
		byte += str(bin[i-1])
		w += 1
		if w == 8:
			print("Byte: ", byte)
			ints.append(byte_to_int(byte))
			byte = ""
			w = 0

	
	for x in range(0, len(ints)):
		dec += str(chr(ints[x]))
		
	return(dec)
	
def main():
	bin = ""
	text = get_text("msg.txt")
	stext = text.split()
	for w in stext:
		if "cyber" in w:
			if w.split("cyber")[1][0]=='-':
				bin += '1'
			else:
				bin += '0'

	text = decode(bin)
	print(str(text))

				
if __name__ == "__main__":
	main()