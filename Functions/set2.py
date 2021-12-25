print("Enter number of elements")
size = int(input())

data = set()

for i in range(size):
    print("Enter element no : ", i+1)
    no = int(input())
    data.add(no)

print("data from set is : ", data)

print("Enter data to search ")
value = int(input())

if value in data:
    print("Element is there")
else:
    print("there is no such element")

