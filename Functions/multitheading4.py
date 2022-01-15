import multiprocessing
import os
import threading


def square(no):
    print("PID is: ", os.getpid())
    return no * no


def main():
    data = [5, 3, 1, 4, 9, 7]

    p = multiprocessing.Pool()

    result = list()

    result = p.map(square, data)

    print("Result is: ", result)


if __name__ == "__main__":
    main()
