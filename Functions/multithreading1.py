import os
import threading


def fun(x):
    print("PID of fun: ", os.getpid())
    print("PPID of fun: ", os.getppid())
    print("Thread name of fun: ", threading.current_thread().name)
    print("Inside fun")
    for i in range(x):
        print("Fun: ", i)


def gun(x):
    print("PID of gun: ", os.getpid())
    print("PPID of gun: ", os.getppid())
    print("Thread name of gun: ", threading.current_thread().name)
    print("Inside gun")
    for i in range(x):
        print("Gun: ", i)


def main():
    no = 5
    print("PID of parent process: ", os.getpid())
    print("thread name of main is: ", threading.current_thread().name)

    thread1 = threading.Thread(target=fun, args=(no,), name="Fun thread")
    thread2 = threading.Thread(target=gun, args=(no,), name="Gun thread")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End of main")


if __name__ == "__main__":
    main()
