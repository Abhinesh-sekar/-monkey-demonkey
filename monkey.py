17#libraires
import numpy as np
import os 

#inputs
j = int(input("enter the key number "))
k = str(input("do you want to import a text file y/n : "))
k.lower()
if k == "y":
    location = input("Enter the location of the file: ")
    with open(location, 'r') as file:
        content = file.read()
        z = list(content)
else:
    z = list(str(input("enter the text lol ")))

#constants
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ','\n']
b = np.load("A:/Encryptions/allthekeyss/allthekeys.npy")
b = list(b[j])

#function
def encryptor(z):
    c = ''
    for i in z:
        index = a.index(i)
        c += b[index]
    return c


en = encryptor(z)

#save the encryprted doc
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "encrypted_message.txt")

with open(output_file, 'w') as file:
    file.write(en)