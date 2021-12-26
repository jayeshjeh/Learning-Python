def Addition(no2, no1):             # function defination
    ans = 0
    ans = no1 + no2
    return ans

def main():
    print("Enter first number")
    v1 = int(input())

    print("Enter second number")
    v2 = int(input())

    # keyword arguments
    ret = Addition(no1=v1, no2=v2)          # function call
    print("Addition is : ", ret)


if __name__ == "__main__":
    main()

