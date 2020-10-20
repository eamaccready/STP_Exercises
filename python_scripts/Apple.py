class Apple():
    def __init__(self, c, w, v, p):
        self.color = c
        self.weight = w
        self.variety = v
        self.price = p


apple1 = Apple("red", "2 oz", "Red Delicious", "$.57")
print(apple1.color)
print(apple1.weight)
print(apple1.variety)
print(apple1.price)
