from itertools import permutations

def solution(numbers):
    perms = permutations(numbers)
    return max([''.join(map(str, perm)) for perm in perms])