from sys import *


def addition(no1, no2):
    ans = no1 + no2
    return ans


def main():
    print('-----------------Marvellous: Automation 1------------------')
    print('Script name: ', argv[0])
    print('Number of arguments accepted: ', len(argv) - 1)

    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid number of arguments")
        print('Use -u flag for usage')
        print('Use -h flag for help')
        exit()

    if argv[1] == '-u' or argv[1] == '-U':
        print("Usage: Script is used to perform the addition of 2 numbers")
        exit()

    if (argv[1] == '-h') or (argv[1] == '-H'):
        print("Help: Name_of_Script First_Argument Second_argument")
        print("First_Argument: Any numeric value")
        print("Second_Argument: Any numeric value")
        exit()

    try:
        ret = addition(int(argv[1]), int(argv[2]))
        print("Addition is: ", ret)

    except Exception:
        print("Exception while executing the script")
        print("Please check the input or contact the developer")


if __name__ == "__main__":
    main()
