l = ['blue', 'white', 'green']

file_path = r"C:\Users\Aisha\Desktop\pp2\LAB_6\files\blahblah.txt"

with open(file_path, 'w+') as f:
    for item in l:
        f.write('%s\n' % item)

print("file written successfully")
