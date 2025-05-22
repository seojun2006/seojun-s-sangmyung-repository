class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.left_top = Point(x1, y1)
        self.right_bottom = Point(x2, y2)

    def show(self):
        print(f"좌측 상단 꼭짓점이 ({self.left_top.x}, {self.left_top.y})이고 "
              f"우측 하단 꼭짓점이 ({self.right_bottom.x}, {self.right_bottom.y})인 사각형입니다.")

    def getWidth(self):
        return self.right_bottom.x - self.left_top.x

    def getHeight(self):
        return self.right_bottom.y - self.left_top.y

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"\n넓이는 {a}, 둘레는 {p}")
