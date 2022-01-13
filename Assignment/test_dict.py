D = {'food': 'rice', 'number': '5', 'color': 'pink'}
print(D['food'])

D['number'] += '6'

print(D)


j = {}
j['name'] = 'Jayesh'
j['age'] = '24'
j['job'] = 'dev'
print(j)


new = dict(name = "bob", job = 'dev', age = 45)
print(new)


jeh = dict(zip(['name', 'job', 'age'], ['lalu', 'testing', '16']))
print(jeh)


rec = {'name': {'first': 'jeh', 'last': 'parmar'},
       'job': {'dev', 'test'},
       'age': 25.36}
print(rec['name'])
print(rec['name']['last'])
print(rec['job'])

rec['job'].add('janitor')
print(rec)
print(rec)
