import wave

def encryption():
	audio = wave.open("cover_audio.wav",mode='rb')
	frames = bytearray(list(audio.readframes(audio.getnframes())))
	lf = len(frames)
	msg = input("Enter a message to hide : ")
	lm = len(msg)
	t1 = int((lf-(lm*8*8))/8)
	msg = msg + t1 *'#'
	arr_bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in msg])))
	for i, bits in enumerate(arr_bits):
	    frames[i] = (frames[i] & 254) | bits
	output_frames = bytes(frames)
	output_name = input("Enter the name of audio file to save the output with extension : ")
	with wave.open(output_name, 'wb') as output:
	    output.setparams(audio.getparams())
	    output.writeframes(output_frames)
	audio.close()
	
def decryption():
	output_name = input("Enter the name of audio file to retrieve the message with extension : ")
	audio = wave.open(output_name, mode='rb')
	frames = bytearray(list(audio.readframes(audio.getnframes())))
	lsb_bytes = [frames[i] & 1 for i in range(len(frames))]
	msg = "".join(chr(int("".join(map(str,lsb_bytes[i:i+8])),2)) for i in range(0,len(lsb_bytes),8))
	output_msg = msg.split("###")[0]
	print("Message extracted from the audio is : \n"+output_msg)
	audio.close()

def main():
	choice = int(input("What Operation to perform ? \n1. Encryption\n2. Decryption\n"))
	if (choice == 1):
		encryption()

	elif (choice == 2):
		decryption()
	else:
		raise Exception("Select from the given choices !!!")

if __name__ == '__main__' :
	main()

