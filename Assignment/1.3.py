
def addition(value1, value2):
    result = value1 + value2

    return result


def main():
    print("Enter First number")
    no1 = int(input())

    print("Enter Second Number")
    no2 = int(input())

    ret = addition(no1, no2)
    print("Addition is : ", ret)


if __name__ == "__main__":
    main()
