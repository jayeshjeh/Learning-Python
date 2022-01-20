import os
import threading


def even():
    for i in range(2, 21, 2):
        print(i)


def odd():
    for i in range(1, 21, 2):
        print(i)


def main():

    thread1 = threading.Thread(target=even, name="even")
    thread2 = threading.Thread(target=odd, name="odd")

    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main()
