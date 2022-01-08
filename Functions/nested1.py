
def outer():
    print("Inside Outer function")

    def inner():
        print("Inside Inner function")

    return inner


def main():
    func_name = outer()     # its call to the outer function
    func_name()             # its call to the inner function
    # inner()


if __name__ == "__main__":
    main()
