import threading


def display(value):
    for i in range(2, (value*2 + 1)):
        if i % 2 == 0:
            print("Number is : ", i)


def main():
    print("How many even numbers want to display")
    size = int(input())

    thread1 = threading.Thread(target=display, args=(size, ))

    thread1.start()


if __name__ == "__main__":
    main()
