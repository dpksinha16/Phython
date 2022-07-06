count= {'raja':1,'bhai':2, 'don':3}
for key in count:
  print(key, count[key])

#retriving value and key
#l=(list(count))
#print(l)
print(count.values())
print(count.keys())
print(count.items())


stuff = dict()
print(stuff.get('candy',-1))