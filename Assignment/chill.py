from functools import reduce


def prime(iNo):

    for i in range(2, iNo):
        if iNo % i == 0:

            return False
        else:

            return True


MultiPly = lambda iNo1: iNo1 * 2


Maximum = lambda iNo1, iNo2: iNo1 if iNo1 > iNo2 else iNo2


def main():

    iValues = int(input("Enter the size of list: "))
    list1 = []

    for i in range(iValues):
        element = int(input("Enter the element: "))
        list1.append(element)

    print("Input List = ", list1)


    filteredData = list(filter(prime, list1))
    print("List after filter = ", filteredData)


    Multi = list(map(MultiPly, filteredData))
    print("List after map = ", Multi)


    Max = reduce(Maximum, Multi)
    print("Output of reduce = ", Max)


if __name__ == "__main__":
    main()
