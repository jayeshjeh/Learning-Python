new = 'Ride the Lightning', 'New toy', 1998

print(new)
# print(new[0])
# print(new[1])
# print(new[2])

title, artist, year = new
print(title)
print(artist)
print(year)

new1 = list(new)
print(new1)

new1[1] = "Hello Jayesh"
print(new1)

table = ("coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)
