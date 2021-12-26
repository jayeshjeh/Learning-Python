
def fun(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j, end=" ")
        print()

def main():
    print("Enter number of rows")
    no = int(input())

    fun(no)

if __name__ == "__main__":
    main()