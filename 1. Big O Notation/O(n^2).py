def print_items(n):
    for i in range(n):
        for j in range(n):
            #for k in range(n):      # O(n^3) -> O(n^2)
            print(i, j)  

    for k in range(n):      # Drop Non Dominant Terms : O(n^2 + n) -> O(n^2)
        print(k)

print_items(10)