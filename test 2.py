class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
      
    a=list(A)
    b=list(B)
    c=b[0]
    

    for i in range(1,len(a)) : 
         if a[i]==c:
            print(i)
            break
         else:
            print(-1)
            break
