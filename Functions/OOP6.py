class Demo:
    A = 10                       # class variable

    def __init__(self):
        print("Inside constructor")
        self.B = 20             # instance variable

    def fun_instance(self):     # instance method
        print("Inside instance method")
        print(self.B)
        print(self.A)
        print(Demo.A)              # correct way to access class variable

    @classmethod
    def fun_class(cls):         # class method
        print("Inside class method")
        print(cls.A)
        print(Demo.A)
        #print(cls.B)

    @staticmethod
    def fun_static():       # static method
        print("Inside static method")

def main():


    obj = Demo()                   # object creation
    #obj.fun_instance()

    Demo.fun_class()


if __name__ == "__main__":
    main()


