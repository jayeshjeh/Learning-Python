def star(value):
    for i in range(value):
        print("*", end='')


def main():
    print("Enter number")
    no = int(input())

    star(no)


if __name__ == "__main__":
    main()
