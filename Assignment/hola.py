def fun(no):
    num = 0
    for a in no:
        num = num + 1
    print("Total ", num)

    numbers = "1,987,284,396,456"
    print(numbers[1 :: 4])

def main():
    String = input()

    fun(String)

if __name__ == "__main__":
    main()

