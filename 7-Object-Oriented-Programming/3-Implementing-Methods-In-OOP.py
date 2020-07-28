class Teddy:
    quantity = 200

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_color(self, color):
        self.color = color

    def change_name(self, name):
        self.name = name

teddy1 = Teddy("Ted", "Red")
print(teddy1.name)
print(teddy1.color)

teddy1.change_name("Janak")
teddy1.change_color("Orange")
print(teddy1.name)
print(teddy1.color)

