def Fact(num):
    plus = 0
    for i in range(1, num):
        if num % i == 0:
            plus = plus + i
    print(plus)


def main():
    print("Enter number : ")
    no = int(input())

    Fact(no)


if __name__ == "__main__":
    main()
