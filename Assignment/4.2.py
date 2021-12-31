def gun(no1, no2):
    return lambda no1, no2: no1 * no2

def main():
    no1 = int(input("Enter first number"))
    no2 = int(input("Enter second number"))


    x = lambda no1, no2 : no1 * no2

    newdata = gun(no1, no2)
    print(newdata)


if __name__ == "__main__":
    main()

