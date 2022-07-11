from operator import index


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
      
     a=list(A)
     b=list(B)
     c=b[0]
     index=-1

     for i in range(1,len(a)) : 
         if a[i]==c:
            index= i
            break
         
     return index
