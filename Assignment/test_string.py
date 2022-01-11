J = 'Jayesh'
print(len(J) - 1)
print(J[len(J)- 1])

print(J[1:3])
print(J[1:])
print(J[:])
print(J + 'xyz')
print(J[0:len(J)])
print('*' * 15)


J = 'z' + J[1:]
print(J)
print('*' * 10)

jet = "Studies"
J = list(jet)
print(J)

J[1] = 'j'
print(J)
print("************")

lol = bytearray(b'spam')
lol.extend(b'name')
print(lol)

print(lol.decode())


