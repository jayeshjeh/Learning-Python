def Star(value):
    for i in range(value):
        print("* ")


def main():
    print("Enter number")
    no = int(input())

    ret = Star(no)

if __name__ == "__main__":
    main()