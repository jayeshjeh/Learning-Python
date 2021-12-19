
# List
# Sequential
# Indexed
# Mutable
Data = [11, 21, 51, 101]

print("Data type is ", type(Data))
print("Length of list is ", len(Data))
print("Actual Data is :", Data)

print("Data from 0th index : ", Data[0])
print("Data from 3rd index : ", Data[-1])

Data[0] = 12
print("New data is : ", Data[0])

Data.append(111)
print(Data)