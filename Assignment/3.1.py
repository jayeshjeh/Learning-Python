def fun(v1):
    data = []

    for i in range(v1):
        print("Enter numbers : ")
        num = int(input())
        data.append(num)

    print(data)
    print(type(data))
    print("Addition is ", sum(data))

    sull = 0
    for i in range(v1):
        sull = sull + data[i]

    print("Addition is : ", sull)

def main():
    print("Enter the length of numbers")
    no1 = int(input())

    ret = fun(no1)

if __name__ == "__main__":
    main()
