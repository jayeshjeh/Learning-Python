def fun(a):
    if a > 0:
        print("*\t", end="")
        a = a - 1
        fun(a)


def main():
    print("Enter number to print star: ")
    n = int(input())

    vet = fun(n)


if __name__ == "__main__":
    main()
