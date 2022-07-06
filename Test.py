class Solution:
    # @param A : list of integers
     # @return an list of long
    def solve(self, A):
        
        n=len(A)
        ans=[]
        for i in range(n):
            ans.append(A[i]*A[i])
            
        return ans