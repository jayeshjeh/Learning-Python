
j = (1, 2, 3, 4)
print(len(j))


print(j + (5, 6))

print(j[2])

print(j.index(1))
print(j.count(3))

j = (2, ) + j[1:]
print(j)

