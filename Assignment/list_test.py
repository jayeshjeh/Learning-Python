J = [123, 'xyz', 3.14]
print(len(J))

print(J[-1])
print(J + [5, 6, 7])
print(J * 2)
J.append("Jayesh")
print(J)
print(J)

J.pop(2)
print(J)

print(J.pop(0))
print(J)
J.sort()
print(J)

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

print(data)

# del data[0:2]
# print(data)

min_v = 100
max_v = 200

stop = 0
for i, x in enumerate(data):
    if x >= min_v:
        stop = i
        break

print(stop)
del data[:stop]
print(data)

start = 0
for i in range(len(data)-1, -1, -1):
    if data[i] <= max_v:
        start = i + 1
        break

print(start)
del data[start:]
print(data)

data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
