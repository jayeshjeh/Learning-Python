power = lambda a: 2**a


def main():
    print("Enter first number: ")
    no1 = int(input())

    ret = power(no1)

    print("Result is: ", ret)


if __name__ == "__main__":
    main()
