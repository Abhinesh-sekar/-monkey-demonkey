import os
import numpy as np

# Constants
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ','\n']
j = int(input("enter the key number"))
b = path = os.path.dirname(__file__)
b = "A:\\Encryptions\\allthekeyss\\allthekeys.npy"
b = np.load(b)
b = list(b[j])
# Inputs


def decrypt(z):
    c = ''
    for i in z:
        if i in b:
            index = b.index(i)
            c += a[index]
        else:
            c += i  # If character is not in the list, leave it unchanged
    return c

# Input string to decrypt
k = str(input("do you want to import a text file y/n : "))
k.lower()
if k == "y":
    location = input("Enter the location of the file: ")
    with open(location, 'r') as file:
        content = file.read()
        z = list(content)
else:
    z = input("Enter the string to be decrypted: ")




# Decryption and output
de = decrypt(z)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "decrypted_message.txt")

with open(output_file, 'w') as file:
    file.write(de)
