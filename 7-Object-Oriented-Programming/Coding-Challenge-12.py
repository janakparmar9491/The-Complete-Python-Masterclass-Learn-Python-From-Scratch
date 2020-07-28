class Computer:

    def getspecs(self, size, weight):
        self.size = size
        self.weight = weight

    def displayspecs(self):
        print(self.size)
        print(self.weight)

class Desktop(Computer):
    def color(self):
        print("The color is black.")

class Laptop(Computer):
    def color(self):
        print("The color is siliver.")

desktop = Desktop()
desktop.color()
desktop.getspecs(19, 15)
desktop.displayspecs()

laptop = Laptop()
laptop.color()
laptop.getspecs(21, 7)
laptop.displayspecs()