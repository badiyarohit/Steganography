import numpy as np
import cv2
from math import log10, sqrt

def calculate_PSNR(input_img, output_img):
	MSE = np.mean((input_img - output_img) ** 2)
	if(MSE == 0): 
		return 100
	max_pixel = 255.0
	PSNR = 20 * log10(max_pixel / sqrt(MSE))
	return PSNR

unicode1 = {}
unicode2 = {}

for i in range(255):
	unicode1[chr(i)] = i
	unicode2[i] = chr(i)

inpnum = int(input("Which image do you want to use ? (Kindly Enter 1 or 2 only)\n1. Cover_1.png \n2. Cover_2.png \n"))
input_img_name = ''
if(inpnum == 1):
	input_img_name = 'Cover_1.png'
if(inpnum == 2):
	input_img_name = 'Cover_2.png'
input_img = cv2.imread(input_img_name)
input_img1 = cv2.imread(input_img_name)

i = input_img.shape[0]
j = input_img.shape[1]

enc_key = '21CS06006'
msg = input("Enter text message to hide : ")

plane = 0
row = 0
column = 0
kl = 0
l = len(msg)

for i in range(l):
	input_img[row,column,plane] = unicode1[msg[i]] ^ unicode1[enc_key[kl]]
	row = row + 1
	column = column + 1
	column = (column+1) % 3 
	kl = (kl+1)%len(enc_key)

output_img_name = input("Enter a name for the output image file : ")
cv2.imwrite(output_img_name,input_img) 
print("Data Hiding in Image completed successfully.")

plane = 0
row = 0
column = 0
kl = 0
l = len(msg)
ch = input("Do you want to extract data from Image (enter y for yes ) : ")

if ch == 'y':
	dec_key = input("Please enter the key to extract text : ")
	dec_msg = ""

	if (enc_key == dec_key) :
		for i in range(l):
			dec_msg += unicode2[input_img[row,column,plane] ^ unicode1[enc_key[kl]]]
			row = row + 1
			column = column + 1
			column = (column+1) % 3
			kl = (kl+1) % len(enc_key)
		print("Encrypted text was : ",dec_msg)
	else:
		print("Key doesn't matched.")
  
	
output_img_name = cv2.imread(output_img_name)
image1 = input_img1
image2 = output_img_name
psnr_value = calculate_PSNR(image1, image2)
print(f"PSNR value is {psnr_value} dB")
