def fact(x):

  
 if x == 1:
  return 1
 else:
  return x * fact(x-1)

print(fact(5))


def countdown(i):
 print (i)
 if i >= 10: #Base case
  return
 else: #Recursive case
  countdown(i+1)

print((countdown(5)))


def greet(name):
 print (hello ,  + name )
 greet2(name)
 print ( getting ready to say bye...)
 bye()
