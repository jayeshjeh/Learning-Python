def gun(value):
    for i in range(2, value+1, 4):
        print(i)

def main():
    print("Enter number")
    no = int(input())

    gun(no)

if __name__ == "__main__":
    main()

