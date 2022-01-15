def fun(no):
    for i in range(no):
        print("*\t" * no)


def main():
    print("Enter number of rows : ")
    yum = int(input())

    fun(yum)


if __name__ == "__main__":
    main()
