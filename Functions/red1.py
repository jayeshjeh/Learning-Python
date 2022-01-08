def display():
    print("using for loop")
    for i in range(4):
        print("Marvellous")


def display_x():
    print("Using while loop")
    i = 0
    while i < 4:
        print("Marvellous")
        i = i + 1


def main():
    display()
    display_x()


if __name__ == "__main__":
    main()
