def main():
    print("Enter the file name that you want to open: ")
    name = input()

    fd = open(name, "rb")
    data = fd.read(5)

    print("Current offset is: ", fd.tell())

    fd.seek(3, 2)
    print("Current offset is: ", fd.tell())

    data = fd.read()

    print(data)


if __name__ == "__main__":
    main()
