
def iteration(no):
    if no >= 0:
        if no > 0:
            print("Positive number")
        else:
            print("Zero")
    else:
        print("Negative number")


def main():

    print("Enter number")
    num = int(input())

    iteration(num)


if __name__ == "__main__":
    main()
