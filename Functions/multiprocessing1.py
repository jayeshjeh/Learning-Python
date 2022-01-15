import os
import multiprocessing


def fun(x):
    print("PID of fun: ", os.getpid())
    print("PPID of fun: ", os.getppid())
    print("Inside fun")
    for i in range(x):
        print("Fun: ", i)


def gun(x):
    print("PID of gun: ", os.getpid())
    print("PPID of gun: ", os.getppid())
    print("Inside gun")
    for i in range(x):
        print("Gun: ", i)


def main():
    no = 5
    print("PID of parent process: ", os.getpid())
    process1 = multiprocessing.Process(target=fun, args=(no,))
    process2 = multiprocessing.Process(target=gun, args=(no,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("End of main")


if __name__ == "__main__":
    main()
