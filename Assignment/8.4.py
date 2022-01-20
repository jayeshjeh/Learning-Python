import os
import threading


def small(strl):
    print("PID of small is: ", os.getpid())
    print("Thread name is: ", threading.current_thread().name)
    icnt = 0
    for i in range(len(strl)):
        if 'a' <= strl[i] <= 'z':
            icnt = icnt + 1
    print("Number of small alphabets are: ", icnt)


def capital(strl):
    print("PID of small is: ", os.getpid())
    print("Thread name is: ", threading.current_thread().name)
    icnt = 0
    for i in range(len(strl)):
        if "A" <= strl[i] <= 'Z':
            icnt = icnt + 1
    print("Number of capital alphabets are: ", icnt)


def digits(strl):
    print("PID of small is: ", os.getpid())
    print("Thread name is: ", threading.current_thread().name)
    icnt = 0
    for i in range(len(strl)):
        if '0' <= strl[i] <= '9':
            icnt = icnt + 1
    print("Number of digits are: ", icnt)


def main():
    string = input("Enter String: ")

    thread1 = threading.Thread(target=small, args=(string, ), name="Small thread")
    thread2 = threading.Thread(target=capital, args=(string, ), name="Capital thread")
    thread3 = threading.Thread(target=digits, args=(string, ), name="Digits thread")

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()
