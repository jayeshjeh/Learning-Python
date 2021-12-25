def Count(string):
    cnt = 0
    for c in string:
        cnt = cnt + 1
    print("Total characters are : ", cnt)



def main():
    String = input("Enter string : ")

    print(len(String))

    ret = Count(String)


if __name__ == "__main__":
    main()