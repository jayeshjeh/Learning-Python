
def main():
    print("Enter the file name that you want to open: ")
    name = input()

    fd = open(name, "r")

    print("Current offset is: ", fd.tell())

    data = fd.read(2)
    print("Data is: ", data)
    print("Current offset is: ", fd.tell())

    fd.seek(3)
    print("Current offset is: ", fd.tell())

    data = fd.read()

    print(data)


if __name__ == "__main__":
    main()
