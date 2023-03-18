import cv2
import string
import os

key = input("Enter Your Secret Key : ")
png_file_path = ""
l=80

# Declaring the essential Characters
dict1 = {}
dict2 = {}
for i in range(255):
    dict1[chr(i)]=i
    dict2[i]=chr(i)
img = cv2.imread(png_file_path)

# Decryption
kl=0
x = 0 # No of rows
y = 0 # no of columns
z = 0 # plane selection

decrypt=""

for i in range(l):
    decrypt+=dict2[img[x, y,z] ^ dict1[key[kl]]]
    y = y+1
    x = x+1
    x = (x+1)%3
    kl = (kl+1)%len(key)
print("Encrypted text was : ", decrypt)
