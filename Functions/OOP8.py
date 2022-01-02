class Demo:
    def __init__(self):
        self.A = 10
        self.__B = 20       # private variable of class         # Abstraction

    def fun(self):
        print("Inside fun")
        self.__gun()

    def __gun(self):
        print("Inside gun")

def main():
    obj = Demo()
    print(obj.A)
    obj.fun()
    # obj.gun()
    # print(obj.__B)            # cant access


if __name__ == "__main__":
    main()

