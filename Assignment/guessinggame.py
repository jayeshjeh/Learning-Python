import random

highest = 100
answer = random.randint(1, highest)
print(answer)
guess = 0
print("Please guess number between 1 and {}".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break

    if guess == answer:
        print("Well done! you guessed it")
        break
    else:
        if guess < answer:
            print("Guess higher")
        else:
            print("Guess Lower")

