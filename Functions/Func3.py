# default argrument
def area(radius, PI = 3.14):
    ans = 0.0
    ans = PI * radius * radius
    return ans


def main():
    print("Enter radius of circle")
    value = float(input())

    # ret = area(value, 7.10)
    ret = area(value)

    print("Area of circle is : ", ret)

if __name__ == "__main__":
    main()


