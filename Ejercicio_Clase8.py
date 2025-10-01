import math
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()

    def compute_length(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        return math.sqrt(dx**2 + dy**2)

    def compute_slope(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        if dx == 0:
            return float('inf')  # vertical line
        angle_rad = math.atan2(dy, dx)
        return math.degrees(angle_rad)

    def compute_horizontal_cross(self):
        return self.start.y * self.end.y <= 0

    def compute_vertical_cross(self):
        return self.start.x * self.end.x <= 0

    def show_info(self):
        print("\nLine Information:")
        print(f"Start point: ({self.start.x}, {self.start.y})")
        print(f"End point: ({self.end.x}, {self.end.y})")
        print(f"Length: {self.length:.2f}")
        print(f"Slope (degrees): {self.slope:.2f}")
        print(f"Crosses x-axis: {self.compute_horizontal_cross()}")
        print(f"Crosses y-axis: {self.compute_vertical_cross()}")


# Rectangle class with 4 initialization methods
class Rectangle:
    def __init__(self, method: int, point1: Point = None, point2: Point = None,
                 width: float = None, height: float = None,
                 line1: Line = None, line2: Line = None,
                 line3: Line = None, line4: Line = None):

        if method == 1:
            self.bottom_left = point1
            self.width = width
            self.height = height
            self.center = Point(point1.x + width / 2, point1.y + height / 2)

        elif method == 2:
            self.center = point1
            self.width = width
            self.height = height
            self.bottom_left = Point(point1.x - width / 2, point1.y - height / 2)

        elif method == 3:
            self.bottom_left = point1
            self.top_right = point2
            self.width = abs(point2.x - point1.x)
            self.height = abs(point2.y - point1.y)
            self.center = Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)

        elif method == 4:
            self.sides = [line1, line2, line3, line4]
            self.bottom_left = line1.start
            self.width = line1.compute_length()
            self.height = line2.compute_length()
            self.center = Point(
                (line1.start.x + line3.end.x) / 2,
                (line1.start.y + line3.end.y) / 2
            )

        else:
            raise ValueError("Invalid method. Use 1, 2, 3 or 4.")

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def show_info(self):
        print("\nRectangle Information:")
        print(f"Bottom-left corner: ({self.bottom_left.x}, {self.bottom_left.y})")
        print(f"Center: ({self.center.x}, {self.center.y})")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {self.compute_area()}")
        print(f"Perimeter: {self.compute_perimeter()}")
print("Choose how to create a rectangle:")
print("1. Bottom-left corner + width and height")
print("2. Center + width and height")
print("3. Two opposite corners")
print("4. Four lines")

method = int(input("Enter method number (1-4): "))

if method == 1:
    x = float(input("Bottom-left X: "))
    y = float(input("Bottom-left Y: "))
    w = float(input("Width: "))
    h = float(input("Height: "))
    rect = Rectangle(1, Point(x, y), width=w, height=h)

elif method == 2:
    x = float(input("Center X: "))
    y = float(input("Center Y: "))
    w = float(input("Width: "))
    h = float(input("Height: "))
    rect = Rectangle(2, Point(x, y), width=w, height=h)

elif method == 3:
    x1 = float(input("First corner X: "))
    y1 = float(input("First corner Y: "))
    x2 = float(input("Opposite corner X: "))
    y2 = float(input("Opposite corner Y: "))
    rect = Rectangle(3, Point(x1, y1), Point(x2, y2))

elif method == 4:
    print("Enter coordinates for 4 points (clockwise or counter-clockwise):")
    x1 = float(input("Point 1 X: "))
    y1 = float(input("Point 1 Y: "))
    x2 = float(input("Point 2 X: "))
    y2 = float(input("Point 2 Y: "))
    x3 = float(input("Point 3 X: "))
    y3 = float(input("Point 3 Y: "))
    x4 = float(input("Point 4 X: "))
    y4 = float(input("Point 4 Y: "))

    l1 = Line(Point(x1, y1), Point(x2, y2))
    l2 = Line(Point(x2, y2), Point(x3, y3))
    l3 = Line(Point(x3, y3), Point(x4, y4))
    l4 = Line(Point(x4, y4), Point(x1, y1))

    rect = Rectangle(4, line1=l1, line2=l2, line3=l3, line4=l4)

else:
    print("Invalid method.")
    exit()

rect.show_info()
