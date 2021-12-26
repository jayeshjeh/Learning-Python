def Addition(no1, no2):             # function defination
    ans = 0
    ans = no1 + no2
    return ans

def main():
    print("Enter first number")
    v1 = int(input())

    print("Enter second number")
    v2 = int(input())

    # positional arguments
    ret = Addition(v1, v2)          # function call
    print("Addition is : ", ret)


if __name__ == "__main__":
    main()

