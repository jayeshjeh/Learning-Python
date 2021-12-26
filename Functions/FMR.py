from functools import reduce

def ChkEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False

def Increment(no):
    return (no + 2)

def Addition(a,b):
    return a + b

def main():
    data = [5, 7, 6, 8, 4]

    print("original data : ", data)

    # filter(function, list)
    newdata = list(filter(ChkEven, data))

    print("Data after filter : ", newdata)

    # map(fucntion, list)
    incrementdata = list(map(Increment, newdata))

    print("Data after map : ", incrementdata)

    ret = reduce(Addition, incrementdata)

    print("Data after reduce : ", ret)

if __name__ == "__main__":
    main()

