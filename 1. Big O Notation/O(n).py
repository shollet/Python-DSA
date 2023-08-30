def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):  # Drop Constants : O(2n) -> O(n)
        print(j)

print_items(10)
