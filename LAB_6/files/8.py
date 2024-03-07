import os

file_path = 'delete.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print(file_path + " has been deleted.")
else:
    print(file_path + " not found.")
