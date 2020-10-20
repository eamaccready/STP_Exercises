class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height)/2


tri1 = Triangle(3,5)
print(tri1.area())
    
