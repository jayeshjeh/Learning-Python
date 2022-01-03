class Circle:
    PI = 3.14

    def __init__(self, area, circum):
        self.a = area
        self.c = circum

    def Accept(self, radius):
        self.r = radius

    def CalculateArea(self):
        result = Circle.PI * (self.r * self.r)
        return result

    def Circumference(self):
        ans = 2 * Circle.PI * self.r
        return ans

def main():

    print("Enter radius")
    Radius = input()
    obj = Circle(Radius)

    obj.Accept()
    ret = obj.CalculateArea()
    print("Area is: ", ret)

    bet = obj.Circumference()
    print("Circumference is: ", bet)


if __name__ == "__main__":
    main()
