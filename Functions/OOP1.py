# encapsulation -> class = characteristics + Behaviour

# class definition
class Arithmatic:
    def __init__(self, a, b):               # constructor | a & b are local variable
        print("Inside init(Constructor)")
        self.no1 = a                        # characteristics
        self.no2 = b                        # characteristics

    def Addition(self):
        ans = self.no1 + self.no2           # ans is local variable.. local means only used within that function
        return ans

def main():

    obj1 = Arithmatic(10, 11)
    ret = obj1.Addition()            # object creation
    print("Addition is: ", ret)

    obj2 = Arithmatic(20, 21)
    ret = obj2.Addition()
    print("Addition is: ", ret)

if __name__ == "__main__":
    main()

