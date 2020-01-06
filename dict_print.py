d = {'anna': 4, 'jan': 5, 'maja': 7}

name = 'anna'
#print(d['anna'])
#print(d[name])

for key in d:
    print(key)
    print(d[key])

print('----')
for key, value in d.items():
    print(key)
    print(value)

print('----')
for value in d.values():
    print(value)


