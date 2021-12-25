def fun(no):
    for i in range(no):
        print("*\t" * no)


def main():
    print("Enter number of rows : ")
    sum = int(input())

    ret = fun(sum)

if __name__ == "__main__":
    main()