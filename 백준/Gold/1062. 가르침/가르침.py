from sys import stdin
from itertools import combinations

def custom_input():
    return stdin.readline().rstrip()

n, k = map(int, custom_input().split())
words = [custom_input()[4:-4] for _ in range(n)]

learned_chars = {'a', 'n', 't', 'i', 'c'}
k -= len(learned_chars)

if k < 0:
    print(0)

elif k == 21:
    print(n)

else:
    remaining_chars = []
    for i in range(26):
        char = chr(i + 97)
        if char not in learned_chars:
            remaining_chars.append(char)

    max_count = 0
    char_combinations = combinations(remaining_chars, k)
    for char_combination in char_combinations:
        count = 0
        for word in words:
            for char in word:
                if char not in char_combination and char not in learned_chars:
                    break
            else:
                count += 1
        max_count = max(count, max_count)

    print(max_count)
