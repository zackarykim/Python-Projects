import math

class Shape:
    def __init__(self, color="blue"):
        self.color = color

    def get_area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, color="blue"):
        super().__init__(color)
        radius = float(input("Enter the radius of the circle: "))
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, color="blue"):
        super().__init__(color)
        side_length = float(input("Enter the side length of the square: "))
        self.side_length = side_length

    def get_area(self):
        return self.side_length**2

    def get_perimeter(self):
        return 4 * self.side_length

class Rectangle(Shape):
    def __init__(self, color="blue"):
        super().__init__(color)
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
circle = Circle()
print("Area of the circle:", circle.get_area())

square = Square()
print("Perimeter of the square:", square.get_perimeter())

rectangle = Rectangle()
print("Area of the rectangle:", rectangle.get_area())