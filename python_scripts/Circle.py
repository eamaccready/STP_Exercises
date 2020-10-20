import math

class Circle():
    def __init__(self, d):
        self.diameter = d

    def area(self):
        return math.pi *((self.diameter/2) **2)


circ1 = Circle(4)
print(circ1.area())
