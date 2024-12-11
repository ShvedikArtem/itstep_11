class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 10)
print("Площа:", rectangle.calculate_area())
print("Периметр:", rectangle.calculate_perimeter())
