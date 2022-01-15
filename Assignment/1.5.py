def iteration(n):
    for i in range(n, 0, -1):
        print(i)


def main():
    print("Enter number: ")
    no = int(input())

    iteration(no)


if __name__ == "__main__":
    main()

# while no > 0:
#   print(no, end="")
#   no = no - 1
