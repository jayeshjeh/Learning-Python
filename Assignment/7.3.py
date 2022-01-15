def fun(n):
    if n >= 1:
        print(n, '\t', end='')
        n -= 1
        fun(n)


def main():
    print("Enter number: ")
    no1 = int(input())

    fun(no1)


if __name__ == "__main__":
    main()
