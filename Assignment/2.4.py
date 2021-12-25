def Fact(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    print(sum)


def main():
    print("Enter number : ")
    no = int(input())

    Fact(no)

if __name__ == "__main__":
    main()