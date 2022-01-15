def fact(value):
    new = 1
    if value < 0:
        print("No Factorial for negative numbers")
    elif value == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, value+1):
            new = new * i
        print("Factorial of ", value, "is", new)


def main():
    num = int(input("Enter a number : "))

    fact(num)


if __name__ == "__main__":
    main()
