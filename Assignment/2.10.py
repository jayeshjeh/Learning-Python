def fun(n):
    count = 0
    while n != 0:
        count = count + (n % 10)
        n = n // 10

    print("Addition of Digits is ", count)


def main():
    print("Enter number")
    no = int(input())

    fun(no)

if __name__ == "__main__":
    main()