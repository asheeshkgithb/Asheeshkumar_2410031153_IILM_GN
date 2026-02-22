class Solution:
    def getMinMax(self, arr):
        minimum = arr[0]
        maximum = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] < minimum:
                minimum = arr[i]
            elif arr[i] > maximum:
                maximum = arr[i]
                
        return [minimum, maximum]
