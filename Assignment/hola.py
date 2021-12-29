
def fun(no):
    num = 0
    for i in range(len(no)):
        print(i, end="")

def main():
    print("Enter string")
    no = input()

    fun(no)

if __name__ == "__main__":
    main()