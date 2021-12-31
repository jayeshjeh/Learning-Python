def fun(v1, v2):
    result = lambda v1, v2 : v1 * v2
    return result

def main():

    num = int(input("Enter number: "))
    no2 = int(input("Enter second number"))

    ret = fun(num, no2)
    print(ret)

if __name__ == "__main__":
    main()

