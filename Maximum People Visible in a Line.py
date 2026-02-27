class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        
        left = [0]*n
        right = [0]*n
        
        stack = []
        
      
        for i in range(n):
            count = 0
            while stack and arr[stack[-1]] < arr[i]:
                count += 1
                stack.pop()
            
            left[i] = count
            stack.append(i)
        
        stack.clear()
        
        
        for i in range(n-1, -1, -1):
            count = 0
            while stack and arr[stack[-1]] < arr[i]:
                count += 1
                stack.pop()
            
            right[i] = count
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] + 1)
        
        return ans
