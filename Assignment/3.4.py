def fun(v1):
    data = []

    for i in range(v1):
        print("Enter numbers : ")
        num = int(input())
        data.append(num)

    print(data)

    print("Enter number to find")
    null = int(input())

    isum = 0
    for i in range(v1):
        if data[i] == null:
            isum = isum + 1

    print("Frequency is : ", isum)


def main():
    print("Enter the length of numbers")
    no1 = int(input())

    fun(no1)


if __name__ == "__main__":
    main()

