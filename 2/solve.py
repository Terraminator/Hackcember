from PIL import Image, ImageChops


def xor(image1, image2):
	r = ImageChops.logical_xor(image1,image2)
	r.save("res.png")
	
def main():
	image1 = Image.open("image.png").convert("1")
	image2 = Image.open("image2.png").convert("1")
	xor(image1, image2)
	
if __name__ == "__main__":
	main()