import os

with open(r'C:\Users\Aisha\Desktop\pp2\LAB_6\files\blahblah.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
