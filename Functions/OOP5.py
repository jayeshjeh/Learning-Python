class Demo:
    A = 10                       # class variable

    def __init__(self):
        print("Inside constructor")
        self.B = 20             # instance variable

    def fun_instance(self):     # instance method
        print("Inside instance method")

        @classmethod
        def fun_class(cls):         # class method
            print("Inside class method")

        @staticmethod
        def fun_static():       # static method
            print("Inside static method")

def main():
    Demo.fun_class()
    Demo.fun_static()

    obj = Demo()                   # object creation
    obj.fun_instance()

    #obj.fun_static()
    #obj.fun_class()

if __name__ == "__main__":
    main()


