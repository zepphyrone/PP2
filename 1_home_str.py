print("Hello World") #1

if 5 > 2:
    print("YES") #2

#Comment   #3
    
"""
This is a comment
written in 
more than just one line
""" #4

carname = "Volvo" #5

x = 50 #6


x = 5
y = 10
print(x + y) #7

x = 5
y = 10
z = x + y
print(z) #8

x, y, z = "Orange", "Banana", "Cherry" #9

x = y = z = "Orange" #10

def myfunc():
  global x
  x = "fantastic" #11
  
x = 5
print(type(x)) #12, output is int

x = "Hello World"
print(type(x)) #13, output is str

x = 20.5
print(type(x)) #14, float

x = ["apple", "banana", "cherry"]
print(type(x)) #15, list

x = ("apple", "banana", "cherry")
print(type(x)) #16, tuple

x = {"name" : "John", "age" : 36}
print(type(x)) #17, dict

x = True
print(type(x)) #18, bool

x = 5
x = float(x) #19

x = 5.5
x = int(x) #20

x = 5
x = complex(x) #21

x = "Hello World"
print(len(x)) #22

txt = "Hello World"
x = txt[0] #23

txt = "Hello World"
x = txt[2:5] #24

txt = " Hello World "
x = txt.strip() #25

txt = "Hello World"
txt = txt.upper() #26

txt = "Hello World"
txt = txt.lower() #27

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}" 
print(txt.format(age))


 

 
  
