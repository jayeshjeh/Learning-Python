
def fun():
    print("Inside fun function")


def gun(func_name):
    print("Inside gun function")
    func_name()


def main():
    gun(fun)


if __name__ == "__main__":
    main()
