import string
import os

directory_path = r"C:\Users\Aisha\Desktop\pp2\LAB_6\files"

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

for letter in string.ascii_uppercase:
    file_path = os.path.join(directory_path, letter + ".txt")
    with open(file_path, "w") as f:
        f.writelines(letter)

