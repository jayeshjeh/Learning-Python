import os
import threading


def chkeven(x):
    if x % 2 == 0:
        return x
    # else :
    # ret =(odd)
    # else:
    # return 'odd'


def even():
    # print("PID of even is:",os.getpid())
    # print("PPID of even is :",os.getppid())
    print("Thread Name:", threading.current_thread().name)
    elist = []
    for i in range(0, 20):
        ret = chkeven(i)
        elist.append(ret)
    print("Even num are:", elist)


def odd():
    # print("PPID of odd is :",os.getppid())
    print("Thread Name:", threading.current_thread().name)


def main():
    print("PID of main :", os.getpid())

    thread1 = threading.Thread(target=even, name="even")
    thread2 = threading.Thread(target=odd, name="odd")

    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main()