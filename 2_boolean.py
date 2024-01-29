print(10 > 9) # 1, True

print(10 == 9) # 2, False

print(10 < 9) # 3, False

print(bool("abc")) # 4, True

print(bool(0)) # 5, False

print(10 * 5) # 6, 50

print(10 / 2) # 7, 8

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!") # 8
  
if 5 != 10:
  print("5 and 10 is not equal") # 9
  
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true") # 10
  
fruits = ["apple", "banana", "cherry"]
print(fruits[1]) # 11

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi" # 12

fruits = ["apple", "banana", "cherry"]
fruits.append("orange") # 13
  
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon") # 14

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") # 15

fruits = ["apple", "banana", "cherry"]
print(fruits[-1]) # 16

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5]) # 17

fruits = ["apple", "banana", "cherry"]
print(len(fruits)) # 18

fruits = ("apple", "banana", "cherry")
print(fruits[0]) # 19

fruits = ("apple", "banana", "cherry")
print(len(fruits)) # 20

fruits = ("apple", "banana", "cherry")
print(fruits[-1]) # 21

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5]) # 22

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!") # 23
  
fruits = {"apple", "banana", "cherry"}
fruits.add("orange") # 24

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) # 25

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") # 26

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") # 27

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model")) # 28

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020 # 29

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red" # 30

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") # 31

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear() # 32

a = 50
b = 10
if a > b:
  print("Hello World") # 33

a = 50
b = 10
if a != b:
  print("Hello World") # 34

a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No") # 35

a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3") # 36
    
if a == b and c == d:
  print("Hello") # 37
  
    
if a == b or c == d:
  print("Hello") # 37


if 5 > 2:
  print("YES") #  38

a = 2
b = 5
print("YES") if a == b else print("NO") # 39

a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES") # 40
    
i = 1
while i < 6:
  print(i)
  i += 1 # 41
  
i = 1
while i < 6:
  if i == 3:
    break
  i += 1 # 42

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # 43
  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") # 44
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) # 45
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # 46
  
for x in range(6):
  print(x) # 47
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) # 48
 