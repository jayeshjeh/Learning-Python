import threading


def display():
    print("Order 1 to 50: ")
    for i in range(1, 51):
        print(i)


def rev():
    print("Reverse 1 to 50: ")
    for i in range(50, 0, -1):
        print(i)


def main():
    thread1 = threading.Thread(target=display)
    thread2 = threading.Thread(target=rev)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()
    print("End of main")


if __name__ == "__main__":
    main()
