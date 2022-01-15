def Fact(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "Is not a prime number")
            print(i, "Times", num // i, "is", num)
            break
    else:
        print(num, "It is a prime number")


def main():
    print("Enter number : ")
    no = int(input())

    Fact(no)


if __name__ == "__main__":
    main()
