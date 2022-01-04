
choice = "-"
while choice != "0":
    if choice in "12345":
        print("You Choose {}".format(choice))
    else:
        print("Choose the option below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGo to Bed")
        print("0:\tExit")

    choice = input()
