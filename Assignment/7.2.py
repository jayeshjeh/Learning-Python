i = 1


def gun(n):
    global i
    if i <= n:
        print(i, '\t', end='')
        i += 1
        gun(n)


def main():
    print("Enter number: ")
    no1 = int(input())

    gun(no1)


if __name__ == '__main__':
    main()
