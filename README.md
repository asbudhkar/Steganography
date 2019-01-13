# LSB Steganography

Python code based on Least Significant Bit Steganography technique to hide text within image. A color pixel is composed RGB components with 24 bits - 8 each for red, green and blue component. The idea is storing information in the LSB bit of B component will differ the decimal value by one in worst case. This difference won't be detected easily by human eye. With more data stored image distortion is more visible.  To make it more secure, user message is encrypted with user defined key.

## Encoding
The message is first encrypted with user key and then LSB technique is used for Stego image generation.

## Decoding
The message is decoded with LSB technique and decrypted with the same key to retrieve hidden text

## Software Used
- Backend: Python 
- Frontend: PyQT

## Installation
This tool requires PyQt and its dependencies.  
pip install PyQt5

## How to run
python back.py




