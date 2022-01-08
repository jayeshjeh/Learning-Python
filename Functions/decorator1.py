def division(a, b):
    ans = 0.0
    ans = a / b
    return ans


def smartdivision(func_name):
    def inner(a, b):                    # passing variable not needed to be different(refer whole code)
        if a < b:
            a, b = b, a
        return func_name(a, b)

    return inner


division = smartdivision(division)


def main():
    a = 0
    b = 0

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    ret = division(a, b)

    print("Division is: ", ret)


if __name__ == "__main__":
    main()
