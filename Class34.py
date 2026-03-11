class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * self.radius * self.radius)
    
    def circumference(self):
        print(2 * 3.14 * self.radius)

circle1 = circle(float(input("Enter the radius of the circle: ")))
print("Area of the circle: ", end="")
circle1.area()
print("Circumference of the circle: ", end="")
circle1.circumference()