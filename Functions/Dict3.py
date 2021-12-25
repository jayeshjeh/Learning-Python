
data = {"A": 10, "B": 20, "C": 30, "D": 40, 51 : "D"}

print("Data is : ", data)
print("Data type is : ", type(data))
print("Length of data is : ", len(data))

# print(data[0])  We cannot access with index

print(data["A"])

for keys in data:
    print(keys, data[keys])
