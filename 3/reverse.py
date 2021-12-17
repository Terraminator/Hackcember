#Reverse

def main():
	text = "R0te Kappe n1x dah1nter"
	ascii_values = ""
	for char in text:
		ascii_values += str(ord(str(char)))
		
	print(ascii_values)

if __name__ == "__main__":
	main()