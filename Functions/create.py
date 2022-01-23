
def main():
    print("Enter the file name that you want to create: ")
    name = input()

    fd = open(name, 'x')

    print("File information is: ", fd)


if __name__ == "_main__":
    main()
