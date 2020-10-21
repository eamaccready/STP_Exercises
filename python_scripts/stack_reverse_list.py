class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def reverse(list):
    stack = Stack()
    result = []
    for item in list:
        stack.push(item)
    while not stack.is_empty():
        result.append(stack.pop())
    return result

to_reverse = [1, 2, 3, 4, 5]
print(reverse(to_reverse))
