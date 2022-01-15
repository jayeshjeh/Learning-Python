
def bull(n):
    if n == 1:
        return 1
    else:
        return n * bull(n - 1)


def main():
    print('Enter number: ')
    no1 = int(input())

    new = bull(no1)
    print("Factorial is: ", new)


if __name__ == "__main__":
    main()
