from itertools import combinations

class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        
        
        if total % 2 != 0:
            return []
        
        target = total // 2
        
        
        if n % 2 == 0:
            sizes = [n // 2]
        else:
            sizes = [n // 2, n // 2 + 1]
        
        for size in sizes:
            for comb in combinations(range(n), size):
                subset1 = [arr[i] for i in comb]
                if sum(subset1) == target:
                    used = set(comb)
                    subset2 = [arr[i] for i in range(n) if i not in used]
                    return [subset1, subset2]
        
        return []
