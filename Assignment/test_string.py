J = 'Jayesh'
print(len(J) - 1)
print(J[len(J) - 1])

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
print('****************')


jeh = 'keyboard'
print(jeh.find('ard'))      # index position of first letter of find
print(jeh)

print(jeh.replace('key', 'lock'))
print(jeh)                  # strings are immutable
print(jeh.upper())
print(jeh.isalpha())
print(jeh.isascii())
print(jeh.__add__('jayesh'))
print(help(jeh.replace))

line = 'abc, xyz, ghj, iop  h'
print(line.split(','))
print(line.rstrip().split(','))
# print(dir(line))

print(u'x' + 'y')

new = 'JayeshParmar'
print(len(new))

new1 = 'Supriya'
print(new + ' ' + new1)

now = 'bazinga'
print(now[2:-1])
now = 'bazinga'
print(now.lower())
print(now.upper())
print(now.rstrip())
print(now.lstrip())
print(now.strip())
print(now.startswith('ba'))
print(now.endswith('zinga'))
print(now.startswith('Baz'))
print(now.endswith('zingA'))

