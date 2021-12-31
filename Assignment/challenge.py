name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age <= 31:
    print("Welcome to holidays, {0} ".format(name))
else:
    print("Sorry you are not old enough")