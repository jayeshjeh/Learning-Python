def main():
    fees = [12500, 15000, 21000, 15500]

    print(fees)

    print("Please enter batch name")
    batch = input()

    print("Thankyou for selecting : ", batch)
    if batch == "PPA":
        print("Fees is : ", fees[1])
    elif batch == "LSP":
        print("Fees is : ", fees[2])
    elif batch == "Python":
        print("Fees is : ", fees[0])
    elif batch == "Angular":
        print("Fees is : ", fees[3])
    else:
        print("There is no such batch in Marvellous")

if __name__ == "__main__":
    main()