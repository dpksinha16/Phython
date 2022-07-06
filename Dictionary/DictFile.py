count=dict()
print("enter line of code")
line=input()
words=line.split()
print("word:", words)

count=dict()
for word in words:
    count[word]=count.get(word,0) +1
print(count)


days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

