class Circle:
    PI = 3.14

    def __init__(self, area, circum):
        self.a = area
        self.c = circum

    def accept(self, radius):
        self.r = radius

    def calculateArea(self):
        result = Circle.PI * (self.r * self.r)
        return result

    def circumference(self):
        ans = 2 * Circle.PI * self.r
        return ans

def main():

    print("Enter radius")
    Radius = input()
    obj = Circle(Radius)

    obj.accept()
    ret = obj.calculateArea()
    print("Area is: ", ret)

    bet = obj.circumference()
    print("Circumference is: ", bet)


if __name__ == "__main__":
    main()
