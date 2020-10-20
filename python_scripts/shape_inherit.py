class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape.")



class Rectangle(Shape):
    def __init__(self, l, w):
        self.length =l
        self.width = w

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def what_am_i(self):
        print("I am a rectangle.")

class Square(Shape):
    def __init__(self, s):
        self.side = s
    
    def calculate_perimeter(self):
        return 4* self.side

    def change_size(self, delta):
        if delta >= 0:
            self.side = self.side + delta
        else:
            self.side = self.side - (-1 * delta)

    def what_am_i(self):
        print("I am a square.")

sh1 = Shape()
r1 = Rectangle(3,5)
s1 = Square(4)

sh1.what_am_i()
r1.what_am_i()
s1.what_am_i()


