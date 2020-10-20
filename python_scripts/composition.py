# Composition classes. A horse "as a" rider.

class Rider():
    def __init__(self, name):
        self.name = name

class Horse():
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider

ride1 = Rider("Bob")
horse1 = Horse("Lucky", "Quarter Horse", ride1)


print(horse1.rider.name)
