
def outer():
    print("Inside Outer function")

    def inner():
        print("Inside Inner function")

    return inner


def main():
    func_name = outer()
    func_name()


if __name__ == "__main__":
    main()
