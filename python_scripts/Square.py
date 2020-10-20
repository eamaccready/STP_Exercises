class Square():
    def __init__(self, s):
        self.side = s
    
    def calculate_perimeter(self):
        return 4* self.side

    def change_size(self, delta):
        if delta >= 0:
            self.side = self.side + delta
        else:
            self.side = self.side - (-1 * delta)


s1 = Square(4)
s1.change_size(2)
print(s1.side)

