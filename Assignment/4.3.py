from functools import reduce

def main():
    print("Enter length of numbers")
    no1 = int(input())

    data = []

    for i in range(no1):
        print("Enter number")
        v1 = int(input())
        data.append(v1)

    print("Original Data: ", data)

    newdata = list(filter(lambda no: 70 <= no <= 90, data))
    print("Data after filter: ", newdata)

    incrementdata = list(map(lambda no: no +10, newdata))
    print("Data after map: ", incrementdata)

    ret = reduce(lambda a, b: a*b,incrementdata)
    print("Data after reduce: ",ret)


if __name__ == "__main__":
    main()