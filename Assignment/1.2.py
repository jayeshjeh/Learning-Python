def chknum(value):
    if value % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


def main():

    print("Enter number")
    no = int(input())

    chknum(no)


if __name__ == "__main__":
    main()
