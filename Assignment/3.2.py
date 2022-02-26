def fun(v1):
    data = []

    for i in range(v1):
        print("Enter numbers : ")
        num = int(input())
        data.append(num)

    print(data)
    print(type(data))
    print("Maximum num is ", max(data))

    mx = data[0]

    for x in data:
        if x > mx:
            mx = x

    print("Maximum number is : ", mx)


def main():
    print("Enter the length of numbers")
    no1 = int(input())

    fun(no1)


if __name__ == "__main__":
    main()

