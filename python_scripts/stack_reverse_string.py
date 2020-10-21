class Stack():
    def __init__(self):
        self.items=[]
        
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
                 
def reverse(string):
    result = ""
    stack = Stack()
    for i in string:
        stack.push(i)
    while not stack.is_empty():
        result += stack.pop()
    return result


string1 = "supercalifragtilisticexpialidocious"
print(reverse(string1))
