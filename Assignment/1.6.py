def rec(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")


def main():

    print("Enter number")
    no = int(input())

    rec(no)


if __name__ == "__main__":
    main()
