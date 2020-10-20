class Hexagon():
    def __init__(self, l):
        self.side_length = l

    def calculate_perimeter(self):
        return self.side_length * 6

hex1 = Hexagon(6)
print(hex1.calculate_perimeter())
