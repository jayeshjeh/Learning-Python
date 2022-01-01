from functools import reduce


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

    squrno = list(map(lambda a: (a*a), newdata))
    print("Data after filter: ", squrno)

    ret = reduce(lambda a, b: a + b, squrno)
    print("Data after reduce: ", ret)

if __name__ == "__main__":
    main()