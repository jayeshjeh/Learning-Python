
# List
# Sequential
# Indexed
# Data is Mutable
# List is Mutable
# Allows Duplicate
# Hetrogeneous

Data = [11, 21, 51, 101, 3.14]

print("Data type is ", type(Data))
print("Length of list is ", len(Data))
print("Actual Data is :", Data)

print("Data from 0th index : ", Data[0])
print("Data from 3rd index : ", Data[-1])

Data[0] = 12
print("New data is : ", Data[0])

Data.append(111)
print(Data)

Data.insert(1, 44)
print(Data)

Data.insert(2, 51)
print(Data)

Data.insert(-1, 151)
print(Data)

print(Data[0])
print(Data[1])
print(Data[-1])
print(Data[-2])
