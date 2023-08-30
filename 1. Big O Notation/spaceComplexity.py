def sum(n):
    if n <= 0:
        return 0
    return n + sum(n - 1)

sum(3)

def pair_sum_sequence(n):       # Space complexity : O(1)
    total = 0
    for i in range(n):
        total += pair_sum(i, i+1)
    return total

def pair_sum(a, b):
    return a + b

pair_sum_sequence(4)