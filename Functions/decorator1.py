def division(a, b):
    ans = 0.0
    ans = a / b
    return ans


def smart_division(func_name):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func_name(a, b)

    return inner


Division = smart_division(division)


def main():
    no1 = 0
    no2 = 0

    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    ret = division(no1, no2)

    print("Division is: ", ret)


if __name__ == "__main__":
    main()
