import Arithemetic

def main():
    print("Enter First number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    ret = Arithemetic.Add(no1, no2)
    print("Addition is : ", ret)

    ret = Arithemetic.Sub(no1, no2)
    print("Subtraction is : ", ret)

    ret = Arithemetic.Mult(no1, no2)
    print("Multiplication is : ", ret)

    ret = Arithemetic.Div(no1, no2)
    print("Division is : ", ret)

if __name__ == "__main__":
    main()