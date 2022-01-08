
def display_r(no):
    if no > 0:
        print("Marvellous")
        no = no - 1
        display_r(no)             # recursive call


def main():
    display_r(4)


if __name__ == "__main__":
    main()
