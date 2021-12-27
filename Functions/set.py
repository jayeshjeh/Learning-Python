data = {10, 20, 30, 40}
list = [10, 20, 30, 40]

print("Datatype is : ", type(data))
print("Data from set : ", data)
print("Length is : ", len(data))
print("Data from list : ", list)

print("Data traversal using loop")
for no in data:
    print(no, end="\t")

data1 = {10, 20, 30, 40, 10}        # duplicate element are allowed but stored only once

print("New set is : ", data1)

data2 = {10, 20, 30.5, "Hello", True}

print(data2)
print(data2[0])
