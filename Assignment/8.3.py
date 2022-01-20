import threading


def even(ilist):
    icnt = 0
    for i in range(len(ilist)):
        if ilist[i] % 2 == 0:
            icnt = icnt + ilist[i]
    print("Addition of even numbers from list is: ", icnt)


def odd(ilist):
    icnt = 0
    for i in range(len(ilist)):
        if ilist[i] % 2 != 0:
            icnt = icnt + ilist[i]
    print("Addition of even numbers from list is: ", icnt)


def main():
    no1 = int(input("Enter size: "))
    ilist = []

    for i in range(no1):
        data = int(input('Enter element: '))
        ilist.append(data)

    print("Data is: ", ilist)

    thread1 = threading.Thread(target=even, args=(ilist, ))
    thread2 = threading.Thread(target=odd, args=(ilist, ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
