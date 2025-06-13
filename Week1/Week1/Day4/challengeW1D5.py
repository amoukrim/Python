import math
import turtle # library for drawing
class Circle: # definition de la classe circle
    
    def __init__(self, *, radius=None, diameter=None):
        if radius is not None: # verifier d'abord si null
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"
    # surcharge des méthodes =, + >, <
    def __add__(self, other): 
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented


#  Test

if __name__ == "__main__":
    c1 = Circle(radius=5)
    c2 = Circle(diameter=10)
    c3 = Circle(radius=3)
    c4 = Circle(diameter=4)

    print(c1)
    print(c2)
    print(f"Are c1 and c2 equal? {c1 == c2}")
    print(f"Is c1 bigger than c3? {c1 > c3}")

    c5 = c1 + c3
    print(f"c1 + c3 = {c5}")

    # Sorting
    circles = [c1, c2, c3, c4, c5]
    circles.sort()
    print("\nSorted Circles by Radius:")
    for c in circles:
        print(c)
      #Bonus: Draw Sorted Circles with Turtle  
        def draw_circle(radius):
            t = turtle.Turtle()
            t.penup()
            t.goto(0, -radius)
            t.pendown()
            t.circle(radius)
            t.hideturtle()

# Draw all circles
if __name__ == "__main__":
    for c in circles:
        draw_circle(c.radius)
    turtle.done()