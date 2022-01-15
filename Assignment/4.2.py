power = lambda a, b: a*b


def main():
    print("Enter first number: ")
    no1 = int(input())

    print("Enter second number")
    no2 = int(input())

    ret = power(no1, no2)

    print("Result is: ", ret)


if __name__ == "__main__":
    main()
