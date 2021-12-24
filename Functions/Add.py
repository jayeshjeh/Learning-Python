import Marvellous1
#def Addition(value):
   # sum = 0
   # i = 0
   # for i in range(len(value)):
        #sum = sum + value[i]

    #return sum



def main():
    size = 0
    i = 0
    Data = []

    print("How many elements you want?")
    size = int(input())

    print("Enter elements : ")
    for i in range(size):
        Data.append(int(input()))

    print("Your entered data is : ", Data)

    ret = Marvellous1.Addition(Data)
    print("Addition is : ", ret)

if __name__ == "__main__":
    main()