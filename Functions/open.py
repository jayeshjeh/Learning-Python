
def main():
    print("Enter the file name that you want to open: ")
    name = input()

    fd = open(name, 'w')

    print("Enter the data which u want to write")
    data = input()

    fd.write(data)
    fd.close()


if __name__ == "__main__":
    main()
