# Inheritance way.

class Rectangle():
    def __init__(self, l, w):
        self.length =l
        self.width = w

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def calculate_perimeter(self):
        return 4* self.length


r1 = Rectangle(3,6)
s1 = Square(4,4,)

print(r1.calculate_perimeter())
print(s1.calculate_perimeter())
