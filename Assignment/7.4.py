
def bull(n):
    if n < 10:
        return n
    else:
        return n % 10 + bull(n // 10)


def main():
    print('Enter number: ')
    no1 = int(input())

    new = bull(no1)
    print("Addition is: ", new)


if __name__ == "__main__":
    main()
