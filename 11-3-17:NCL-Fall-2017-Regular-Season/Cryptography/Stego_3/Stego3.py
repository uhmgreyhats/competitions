from PIL import Image
data = ""

with open("Stego 3.txt", "r") as f:
	for line in f:
		hex_input= line.split("#",1)[1] 
		dec_output = [
			 int(hex_input[0:2], 16), int(hex_input[2:4], 16),
			 int(hex_input[4:6], 16),
		]
		data += chr(dec_output[0]) + chr(dec_output[1]) + chr(dec_output[2])
im = Image.frombytes("RGB", (444,299), data)
im.save("Stego.png", "PNG")
