class Shape:
    are = 0
    def area(self):
        print(self.are)

class Rectangle(Shape):
    def __init__(self, length, wight):
        self.length = length
        self.wight = wight
  
    def area(self):
        print(self.length * self.wight)

a = Shape()
b = Rectangle(2, 3)

a.area()
b.area()