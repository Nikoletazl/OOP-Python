class Glass():
    capacity = 250

    def __init__(self):
        self.content = 0

    def get_space_left(self):
        return self.capacity - self.content

    def fill(self, quantity):
        if self.get_space_left() < quantity:
            return f"Cannot add {quantity} ml"

        self.content += quantity
        return f"Glass filled with {quantity} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.get_space_left()} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
