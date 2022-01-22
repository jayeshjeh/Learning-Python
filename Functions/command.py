from sys import *


def main():
    print("Number of command line arguments are: ", len(argv))
    print("Name of Application is: ", argv[0])
    print(type(argv[1]))

    ans = int(argv[1]) + int(argv[2])

    print(ans)


if __name__ == "__main__":
    main()
