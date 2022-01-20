import threading


def even(x):
    isum = 0
    for i in range(1, x):
        if x % i == 0:
            isum = isum + i
    print("Addition of even factors is: ", isum)


def odd(n):
    isum = 0
    for i in range(1, n):
        if n % i != 0:
            isum = isum + i
    print("Addition of odd factors is: ", isum)


def main():
    no1 = int(input("Enter the number: "))

    thread1 = threading.Thread(target=even, args=(no1,))
    thread2 = threading.Thread(target=odd, args=(no1,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
