def fun(n):
    count = 0
    while n != 0:
        n = n // 10
        count = count + 1

    print("Number of Digits are ", str(count))


def main():
    print("Enter number")
    no = int(input())

    fun(no)

if __name__ == "__main__":
    main()