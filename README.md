# LSB Steganography
Python code based on Least Significant Bit Steganography technique to hide text within image. A color pixel is composed RGB components with 24 bits- 8 each for red, green and blue respectively. The idea is storing information in the LSB bit of B component will will differ the decimal value by one in worst case. This difference won't be detected easily by human eye. With more data stored image distortion is more visible. To make it more secure, user message is encryption with user defined key. This message is used to form Stego image 

## Installation
This tool requires PyQt and its dependencies
pip install PyQt5

## Software Used
- Backend: Python 
- Frontend: PyQT

## How to run
python back.py




