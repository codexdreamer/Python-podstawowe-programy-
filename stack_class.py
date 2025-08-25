class Stack:
    def __init__(self):
        self.dane = []
        self.limit = 10

    def push(self, element):
        if len(self.dane) < self.limit:
            self.dane.append(element)
            print(self.dane)
        else:
            raise Exception("Stos jest pełny!")

    def pop(self):
        if not self.is_empty():
            return self.dane.pop()
        else:
            raise Exception("Stos jest pusty!")

    def is_empty(self):
        return len(self.dane) == 0



stos = Stack()
stos.push(5)
stos.push(10)
print(stos.pop())
print(stos.is_empty())
