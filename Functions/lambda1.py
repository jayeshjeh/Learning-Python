# named function
def Add(a, b):
    return a + b

# lambda function
AddX = lambda a, b : a+b

def main():
    ret = Add(10, 20)
    print("Addition is : ", ret)

    ret = AddX(10, 30)
    print("Addition is : ", ret)
    print(type(Add))
    print(type(AddX))
    print(lambda a, b : a+b)

if __name__ == "__main__":
    main()



