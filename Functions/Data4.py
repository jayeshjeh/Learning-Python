
# List
# Sequential
# Indexed
# Data is Mutable
# List is Mutable
# Allows Duplicate
# Hetrogeneous

Data = [11, 21, 51, 101]

print("Data using while loop")
i = 0

# while(i < 4):


while(i < len(Data)):
    print(Data[i])
    i = i + 1

print("Data using for loop")

# for i in range(4):


for i in range(len(Data)):
    print(Data[i])

