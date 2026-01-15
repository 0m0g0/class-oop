import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # 面積 = πr²（小数第2位まで）
        return round(math.pi * self.radius**2, 2)

    def perimeter(self):
        # 周囲長 = 2πr（小数第2位まで）
        return round(2 * math.pi * self.radius, 2)


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85


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


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        # 面積 = 一辺²（小数第2位まで）
        return round(self.side**2, 2)

    def diagonal(self):
        # 対角線 = 一辺 × √2（小数第2位まで）
        return round(self.side * math.sqrt(2), 2)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21


class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1


counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7

counter2.count_up()
print(counter2.value)  # 8

counter2.count_up()
print(counter2.value)  # 9


class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step


counter1 = MyCounterV2(value=0, step=1)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV2(value=0, step=3)
print(counter2.value)  # 0

counter2.count_up()
print(counter2.value)  # 3

counter2.count_up()
print(counter2.value)  # 6


class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

    def count_down(self):
        self.value -= self.step


counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 3

counter1.count_up()
print(counter1.value)  # 5

counter1.count_down()
print(counter1.value)  # 3

counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3

counter2.count_down()
print(counter2.value)  # -1

counter2.count_down()
print(counter2.value)  # -5
