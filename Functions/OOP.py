# encapsulation -> class = characteristics + Behaviour

# class definition
class Arithmatic:
    def __init__(self, a, b):               # constructor
        print("Inside init(Constructor)")
        self.no1 = a                        # characteristics
        self.no2 = b                        # characteristics

    def Addition(self):
        ans = self.no1 + self.no2
        return ans

def main():
    print("Enter first number")
    x = int(input())

    print("Enter second number: ")
    y = int(input())

    obj = Arithmatic(x, y)
    ret = obj.Addition()            # object creation

    print("Addition is: ", ret)

if __name__ == "__main__":
    main()

