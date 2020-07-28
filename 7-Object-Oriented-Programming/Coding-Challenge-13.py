class Number:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x

numa = Number(3)
numb = Number(4)
print(numa * numb)