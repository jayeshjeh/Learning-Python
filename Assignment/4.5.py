from functools import reduce


def primenumber(no):
    for i in range(2, no):
        if no % i == 0:
            return False
        else:
            return True


mult = lambda no: (no*2)


maximum = lambda a, b: a if a > b else b


def main():
    print("Enter length of numbers")
    no1 = int(input())

    data = []

    for i in range(no1):
        print("Enter numbers ")
        no = int(input())
        data.append(no)

    print("Input data is: ", data)

    newdata = list(filter(primenumber, data))
    print("Data after filter: ", newdata)

    squrno = list(map(mult, newdata))
    print("Data after filter: ", squrno)

    ret = reduce(maximum, squrno)
    print("Data after reduce: ", ret)


if __name__ == "__main__":
    main()
