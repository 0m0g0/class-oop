import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        # 面積 = 縦 × 横（小数第2位まで）
        return round(self.height * self.width, 2)

    def diagonal(self):
        # 対角線 = √(縦² + 横²)（小数第2位まで）
        return round(math.sqrt(self.height**2 + self.width**2), 2)


rectangle1 = Rectangle(height=5, width=6)
print(f"{rectangle1.area():.2f}")  # 30.00
print(f"{rectangle1.diagonal():.2f}")  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(f"{rectangle2.area():.2f}")  # 9.00
print(f"{rectangle2.diagonal():.2f}")  # 4.24
