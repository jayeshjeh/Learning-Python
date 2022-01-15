import os
import threading

def square(no):
    return no * no


def main():
    data = [5, 3, 1, 4, 9, 7]

    result = []

    for i in range(len(data)):
        result.append(square(data[i]))

    print("Result is: ", result)


if __name__ == "__main__":
    main()
