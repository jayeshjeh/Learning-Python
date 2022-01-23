def main():
    print("Enter the file name that you want to open: ")
    name = input()

    fd = open(name, 'a')

    print("Enter the data which u want to append")
    data = input()

    fd.write(data)
    fd.close()


if __name__ == "__main__":
    main()
