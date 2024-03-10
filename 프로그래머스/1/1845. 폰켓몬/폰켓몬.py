def solution(nums):
    result = 0
    
    set_nums = set(nums)
    n = len(nums)
    ll = len(set_nums)
    
    if ll < n // 2:
        return ll
    else:
        return n // 2

