menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if 'spam' not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}".format(meal, meal.count("spam")))


menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for i in range(len(meal) - 1, - 1, - 1):
        if meal[i] == "spam":
            del meal[i]

    print(", ".join(meal))

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()
