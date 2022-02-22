# def Maximum(list):
#     max = sum(list)
#
#     avg = max / len(list)
#
#     result = (avg - 32) * (5 / 9)
#
#     print("Result is ", result)
#
#
# def main():
#     list = []
#     size = int(input("Enter size"))
#     for i in range(size):
#         data = float(input())
#         list.append(data)
#
#     Maximum(list)
#
#
# if __name__ == "__main__":
#     main()


def fun(v1):
    data = []

    for i in range(v1):
        print("Enter numbers : ")
        num = float(input())
        data.append(num)

    maxi = sum(data)

    avg = maxi / v1
    print(avg)
    result = (avg - 32) * (0.5555)
    print("Result is ", result)



def main():
    print("Enter the length of numbers")
    no1 = int(input())

    fun(no1)


if __name__ == "__main__":
    main()

