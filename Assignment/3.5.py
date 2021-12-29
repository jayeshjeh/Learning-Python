def fun(v1):
    data = []

    for i in range(v1):
        print("Enter numbers : ")
        num = int(input())
        data.append(num)

    print(data)
    sum = 0
    for i in range(v1):
        if(data[i] % i != 0):
            no2 = data[i]
            sum = sum + no2

    print("Frequency is : ", sum)


def main():
    print("Enter the length of numbers")
    no1 = int(input())

    ret = fun(no1)

if __name__ == "__main__":
    main()

