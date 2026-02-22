class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        min_len = n + 1
       current sum=0
       start =0
       for end in range(n):
           current sum+=arr[end]
           
       
