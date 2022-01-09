class demo:
    def __init__(self):
        self.i = 10
        self.j = 20

    def add(self, a):
        print("Inside add with one parameter")

    def add(self, a, b):
        print("Inside add with two parameters")


def main():
    obj = demo()

    # obj.add(11)
    obj.add(11, 21)


if __name__ == "__main__":
    main()
