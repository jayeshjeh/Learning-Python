def Check(value):
    if(value%5 == 0):
        print("True")
    else:
        print("False")

def main():
    print("Enter number")
    no = int(input())

    ret = Check(no)


if __name__ =="__main__":
    main()