def pair_sum(arr, sum):
    s = set()
    for num in arr:
        if sum - num in s:
            return True
        s.add(num)
    return False
