def count(string):
    cnt = 0
    for c in string:
        cnt = cnt + 1
    print("Total characters are : ", cnt)


def main():
    string = input("Enter string : ")

    print(len(string))

    count(string)


if __name__ == "__main__":
    main()
