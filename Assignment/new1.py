def power(n):
    if n * n == 2 ** n:
        print("it is the power of the number entered")
    else:
        print("Wrong number")


def main():
    print("Enter number: ")
    no1 = int(input())

    power(no1)


if __name__ == "__main__":
    main()
