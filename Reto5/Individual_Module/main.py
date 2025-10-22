import math 
from point import Point
from rectangle import Square
from triangle import EquilateralTriangle


if __name__ == "__main__":
    # Create points for a square with side length 2
    p1 = Point(0, 0)
    p2 = Point(0, 2)
    p3 = Point(2, 2)
    p4 = Point(2, 0)
    square = Square([p1, p2, p3, p4])

    # Create points for an equilateral triangle with side length 2
    t1 = Point(0, 0)
    t2 = Point(2, 0)
    t3 = Point(1, math.sqrt(3))  # height for equilateral triangle
    triangle = EquilateralTriangle([t1, t2, t3])

    # Print the square's information
    print(square)
    print("---------------------------------------------")

    # Print the triangle's information
    print(triangle)
