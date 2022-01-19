import os
import threading


def even(n):
    for i in range(2, n + 1, 2):
        print(i)


def odd(x):
    for i in range(1, x+1, 2):
        print(i)


def main():
    print("PID of parent process: ", os.getpid())
    no1 = 20

    thread1 = threading.Thread(target=even, args=(no1,))
    thread2 = threading.Thread(target=odd, args=(no1,))

    thread1.start()
    thread2.start()

    print("End of main")


if __name__ == "__main__":
    main()
