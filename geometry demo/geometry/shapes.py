from abc import ABC, abstractmethod
import math 
#Triangle and Rectangle
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Compute area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:    
        """Compute perimeter of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, side1: float, side2: float):
        # store side lengths
        self.side1 = side1
        self.side2 = side2
    def area(self) -> float:
        # compute area using width * height
        return self.side1*self.side2
    def perimeter(self) -> float:
        # compute perimeter using (width+height)*2
        return (self.side1+self.side2)*2
class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        # store side lengths
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        # compute area using heron's formula
        s = (self.side1+self.side2+self.side3)/2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def perimeter(self) -> float:
        # compute perimeter by adding all the sides
        return self.side1+self.side2+self.side3