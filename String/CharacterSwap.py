
    
s1=str(input())
s2=str(input())
str=None
'''Input: s1,s2 two strings takes the string as input
       Output: str return the resultant string'''
    
n=len(s1)
a= s1[0:2]
b=s1[2:n]
print(b)

 
y=len(s2)
c=s2[0:2]
d=s2[2:y]
print(d)

s1=c+b
s2=a+d
str=s1 +' '+ s2
    
    
    
    
print(str)  


   