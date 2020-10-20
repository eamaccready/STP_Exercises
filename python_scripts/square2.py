class Square2():
    square_list = []

    def __init__(self, l):
        self.length = l
        self.square_list.append(l)

    def print_sides(self):
        print(self.length)
        print("{} by {} by {} by {}".format(self.length, self.length, self.length, self.length))


s1 = Square2(3)

print(s1.square_list)
s1.print_sides()
