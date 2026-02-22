class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)

        
        if m <= 0 or m > n:
            return -1

        
        arr.sort()

        
        min_diff = arr[m - 1] - arr[0]

        
        for i in range(1, n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff
