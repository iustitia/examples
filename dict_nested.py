d = {'anna': [4, 54, 2, 435], 'jan': [5, 45], 'maja': [7]}

print(d['anna'])

for i in d['anna']:
    print(i)

print('----')

for value in d.values():
   # print(value)
   print(sum(value))

for key in d:
    print(key)
    # print(d[key])
    print(sum(d[key]))
#
#
a = [345, 34, 45, 345]
# x = sum(a)
# print(sum(a))

totalsum = 0
for value in a:
    totalsum += value
