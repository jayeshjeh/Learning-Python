def Add(v1, v2):
    result = v1 + v2
    return result

def main():
    print("Enter number")
    no1 = int(input())

    print("Enter second number")
    no2 = int(input())

    ret = Add(no1, no2)
    print("Addition is : ", ret)

if __name__ == "__main__":
    main()

