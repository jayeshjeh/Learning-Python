def fun(num):
    for i in range(num):
        for j in range(i, num):
            print("*\t", end=" ")
        print("\n")

def main():
    print("Enter the number of rows")
    no = int(input())

    fun(no)

if __name__ == "__main__":
    main()
