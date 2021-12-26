def Add(*value):
    sum = 0
    for i in value:
        sum = sum + i

    return sum

def main():
    ret = Add(10, 20, 30, 40, 50)
    print("Addition is : ", ret)

    ret = Add(10, 20, 30, 40)
    print("Addition is : ", ret)

    ret = Add()
    print("Addition is : ", ret)

if __name__ == "__main__":
    main()

