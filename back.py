# File to perform encoding and decoding

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *	
import sys
import string

# Used to read image
from PIL import Image

# Frontend

import front

ALPHABET = string.ascii_lowercase
CHARACTERS_THAT_MUST_REMAIN_THE_SAME = string.digits + string.punctuation + string.whitespace

class stegano(QtWidgets.QMainWindow, front.Ui_mainWindow):

	def __init__(self, parent=None):
		super (stegano, self).__init__()
		self.setupUi(self)
		self.ebrowse.clicked.connect(self.selectfile1)
		self.dbrowse.clicked.connect(self.selectfile2)
		self.encode.clicked.connect(self.hidetext)
		self.Decode.clicked.connect(self.showtext)
	
	# Select image file to encode

	def selectfile1(self):
		fname1 = QFileDialog.getOpenFileName()
		self.elineEdit.setText(fname1[0])
		self.elabel.setPixmap(QPixmap(fname1[0]))
		self.elabel.setScaledContents(1)

	def selectfile2(self):
		fname2 = QFileDialog.getOpenFileName()
		self.dlineEdit.setText(fname2[0]) 
		self.dlabel.setPixmap(QPixmap(fname2[0]))
		self.dlabel.setScaledContents(1)

	# Covert ASCII message to binary for encoding

	def msgtobin(self,message):
		arr = []
		arr2 = []
		arr = list(map(bin,bytearray(message))) # function 'bin' is operated on each value inside message and list is returned
		for i in range(len(arr)):
			temp=arr[i]
			arr2.append(temp[2:])
		bin_message = ""                       
		for a in arr2:
			a=a.zfill(8)
			bin_message=bin_message + a
		return bin_message[1:]

	# Hide message in image

	def hide(self,image_name,message):
		newimage_data = []
           
           # Cover image 
		image = Image.open(image_name).convert('RGBA')

           # Final message  
		final_message = self.msgtobin(message.encode('utf-8')) + "1111111111111110"
		index = 0
		bnew = 0						#counter needed for indexing in binary message string
		width,height = image.size
		check_val = self.check(width , height , len(final_message))    #check if length of string > max possible length 
		if check_val == 0:
			return None
		else:
			datas = image.getdata()
			for item in datas :
				bhex = hex(item[2])
				bint = item[2]
				if index < len(final_message):
					if bhex[-1] in ("0","1","2","3","4","5"):		
						bnew = self.encodefunc(image,final_message,index,bhex)
						bint = bnew
						index = index + 1
					newimage_data.append((item[0],item[1],bint,255))		
				else:
					newimage_data.append((item[0],item[1],item[2],255))
			
                 # Create Stego-image
			im2 = Image.new(image.mode,image.size)
			im2.putdata(newimage_data)
			im2.save("encodedimage.png","png")					
			return 1        				#encoding successful
						
	# Function to check if message fits in image					 
	def check(self,w,h,str_len):
		if (w*h)/8 < str_len:
			return 0
		else:
			return 1

      # Encode data

	def encodefunc(self,im,message,ind,b):
		bstr = b
		bstr = bstr[:-1]
		bstr = bstr + message[ind]
		return int(bstr,0)
		
      # Hide message by first encrpytion with key and then LSB steganography 
	def hidetext(self):
		image_pt = (str(self.elineEdit.text()))
		message = (str(self.textEdit.toPlainText()))
		keyword = (str(self.epass.text()))
		message = self.encrypt(message,keyword)
		imt = Image.open(image_pt).convert('RGBA')
		retval = self.hide(image_pt,message)
		if retval == 1:
			self.eerror.setText("Encoding successful!")
		else:
			self.eerror.setText("Error occured!")

      # To return the binary character encoded  
	def rgbtohex(self,b):
		bhex=hex(b)
		if bhex[-1] in ("0","1"):
			return bhex[-1]
		else:
			return None;
	
	# Decode message from image	
	def decode(self,filename):
		im=Image.open(filename)
		binary = ''
		flag = 0
		datas = im.getdata()
		w,h=im.size

           # Get hidden message in binary form
 
		for item in datas :
			digit=self.rgbtohex(item[2])
			if digit==None:
				pass
			else:
				binary=binary+digit
				if (binary[-16:] == '1111111111111110'):
					flag = 1
					break
		if flag == 1 :
			binary = binary[:-16]
			message = ""
			i = 0
			while binary != "":
				message = message + str(chr(int(binary[:7], 2)))
				binary = binary[8:]
			self.derror.setText("Decoding successful")
			return (message)
		else :
			self.derror.setText("This is not an encoded image!")

	def showtext(self):
		message = self.decode(str(self.dlineEdit.text()))
		keyword = (str(self.dpass.text()))
		message = self.decrypt(message,keyword)
		self.dtextEdit.setText(message)
	
	def cycle_get(self,lst,index):
	    new_index = index % len(lst)
	    return(lst[new_index])

	def cycle_increment_index(self,index,lst):
	    if index == len(lst) - 1:
	        index = 0
	    else:
	        index += 1
	    return(index)

	def shift(self,letter,value):
	    current_letter_value = ALPHABET.find(letter)
	    end_value = current_letter_value + value
	    return(self.cycle_get(ALPHABET,end_value))

	def convert_key_to_numbers(self,key):
	    return([ALPHABET.find(i) for i in key])

	# Encryption 

	def encrypt(self,text,key,reverse_operation=False):
	    text = text.lower()
	    key = self.convert_key_to_numbers(key)
	    index_of_key = 0
	    result = ""
	    for char in text:
	        if char in CHARACTERS_THAT_MUST_REMAIN_THE_SAME:
	            result += char
	        else:
	            if not reverse_operation:
	                result += self.shift(char,key[index_of_key])
	            else:
	                result += self.shift(char,- key[index_of_key])
	            index_of_key = self.cycle_increment_index(index_of_key,key)
	    return(result)

	def decrypt(self,text,key):
	    return(self.encrypt(text,key,reverse_operation=True))


app = QtWidgets.QApplication(sys.argv)
form = stegano()
form.show()
app.exec_()