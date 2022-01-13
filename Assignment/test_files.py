f = open('lola.py', 'w')
f.write('Hello\n')

f.write("world\n")
f.close()

f = open('lola.py')
text = f.read()
print(text)
print(text.split())

print(dir(f))
print(help(f.seek))

print('***')
for line in open('lola.py'): print(line)

