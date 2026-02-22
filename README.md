import bisect

class Solution:
    def median(self, matrix):
        
        R = len(matrix)
        C = len(matrix[0])
        minimum = matrix[0][0]
        maximum = matrix[0][C - 1]
        
        for i in range(R):
            minimum = min(minimum, matrix[i][0])
            maximum = max(maximum, matrix[i][C - 1])
        
        desired = (R * C) // 2
        
        while minimum < maximum:
            mid = (minimum + maximum) // 2
            place = 0
            
            for i in range(R):
                place += bisect.bisect_right(matrix[i], mid)
            
            if place <= desired:
                minimum = mid + 1
            else:
                maximum = mid
        
        return minimum
