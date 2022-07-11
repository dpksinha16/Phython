class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    #You are given two character strings A and B.

#You have to find the first occurrence of string B in string A, as a substring, and return the starting position of first occurrence.
    def solve(self, A, B):

     for i in range(len(A)-len(B)+1) : 
         if B==A[i:i+len(B)]:
            return (i+1)
     return -1
            