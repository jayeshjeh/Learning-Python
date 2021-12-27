import array as ARR

def main():
    print("Demo of array in python")

    data = ARR.array('f', [10.1, 20.2, 30.3, 40.4, 50.5])

    print(data)

    print("Length of array : ", len(data))
    print("Type is : ", type(data))

    print(data[0])
    print(data[-1])

    print("1st loop")
    for a in range(len(data)):
        print(data[a])

    print("2nd loop")
    for no in data:
        print(no, end="\t")

    print("Typecode of array is ", data.typecode)


if __name__ == "__main__":
    main()
