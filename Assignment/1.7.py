def check(value):
    if value % 5 == 0:
        print("True")
    else:
        print("False")


def main():
    print("Enter number")
    no = int(input())

    check(no)


if __name__ == "__main__":
    main()
