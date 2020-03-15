class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
    	super().__init__(length, length)

r1 = Rectangle(2,4)
print(r1.area())
print(r1.perimeter())

s1 = Square(2)
print(s1.area())
print(s1.perimeter())