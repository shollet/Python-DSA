#  Created by Elshad Karimov on 3/17/20.
#  Copyright © 2020 Elshad Karimov. All rights reserved.


array = [1, 2, 3, 4, 5]

######  Constant time complexity  #######
print('######  Constant time complexity  #######')
print(array[0])


######  Linear time complexity  #######
print('######  Linear time complexity  #######')
for element in array:
     print(element)


######  Logarithmic time complexity  #######
print('######  Logarithmic time complexity  #######')
for index in range(0,len(array),3):
     print(array[index])


######  Quadratic time complexity  #######
print('######  Quadratic time complexity  #######')
for x in array:
    for y in array:
         print(x,y)


######  Exponential time complexity  #######
print('######  Exponential time complexity  #######')
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


######  Add vs Multiply ####### 
arrayA = [1,2,3,4,5,6,7,8,9]
arrayB = [11,12,13,14,15,16,17,18,19] 

for a in arrayA:
    print(a)

for b in arrayB:
    print(b)

for a in arrayA:
    for b in arrayB:
        print(a,b)

######  Iterative algorithm - finding the biggest number in the array ####### 

sample1Array = [1,10,45,33,23,45,67,2,3,33,55,11,65,76,34,35,27,99]

def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1,len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    print(biggestNumber)

findBiggestNumber(sample1Array)

######  Recursive algorithm - finding the biggest number in the array ####### 

def findMaxNumRec(sampleArray, n):
    if n == 1:
       return sampleArray[0]
    return max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1))

print(findMaxNumRec(sample1Array,len(sample1Array)))


######  Recursive algorithm multiple calls ####### 

def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-1)

print(f(3))







######  Quiz Questions ####### 


def f1(n):
    if n <= 0:
        return 1
    else:
        return 1 + f1(n-1)
    
""" The given function `f1(n)` is a simple recursive function that decrements its argument `n` by 1 until `n` becomes less than or equal to 0. For each positive integer value of `n`, the function calls itself once.

Let's analyze the number of times the function gets called:

1. If `n` is 1, then the function gets called 2 times: once with `n=1` and then with `n=0`.
2. If `n` is 2, then the function gets called 3 times: once with `n=2`, then with `n=1`, and then with `n=0`.
3. If `n` is 3, then the function gets called 4 times: once with `n=3`, then with `n=2`, then with `n=1`, and finally with `n=0`.

Continuing this pattern, we can see that for a positive integer value of `n`, the function is called `n + 1` times.

Therefore, the time complexity of this function is O(n), where `n` is the input value to the function. """


def f2(n):
    
    if n <= 0:
        return 1
    else:
        return 1 + f2(n-5)
    
""" In the given function `f2(n)`, the function decrements its argument `n` by 5 in each recursive call until `n` becomes less than or equal to 0. Let's analyze the number of times the function gets called based on the value of `n`:

1. If (n <= 0), the function doesn't recurse; it gets called once.
2. If (1 <= n <= 5), the function gets called twice: once with the original value of `n` and then with (n-5).
3. If (6 <= n <= 10), the function gets called three times: once with the original `n`, then with (n-5), and then (n-10).
4. And so on...

Thus, if n is a multiple of 5, the function will be called (n/5 + 1) times. If n is not a multiple of 5, it will be called a few more times due to the remaining values, but this number will still be proportional to (n/5).

The dominant factor in the time complexity of this function is how many times 5 can be subtracted from n before reaching a value less than or equal to 0. Hence, the time complexity is O(n/5), which is essentially O(n). 

Remember, in big-O notation, constant factors like 1/5 are typically ignored, so we just state the time complexity as O(n). """


def f3(n):
    if n <= 0:
        return 1
    else:
        return 1 + f3(n/5)
    
""" In the given function `f3(n)`, the function divides its argument `n` by 5 in each recursive call until `n` becomes less than or equal to 0. Let's analyze how many times the function gets called:

The function `f3` essentially asks how many times you can divide `n` by 5 before getting a number that is less than or equal to 0.

For simplicity, consider a scenario where `n` is a power of 5, say (n = 5^k) for some integer k:

1. After the first call, n becomes (5^(k-1))
2. After the second call, n becomes (5^(k-2))
3. And so on...

For (n = 5^k), you can call the function (k + 1) times before n becomes less than or equal to 0. Hence, the depth of the recursive call is proportional to (log_5(n)).

So, the time complexity of `f3` is O(log_5(n)). 

However, in the context of big-O notation, logarithms with different bases are equivalent up to constant factors. That is, (log_5(n)) = log(n)/log(5). Since we typically ignore constant factors in big-O notation, the time complexity is often written as O(log(n)). """


def f4(n,m,o):
    if n<=0:
        print(n,m,o)
    else:
        f4(n-1,m+1,o)
        f4(n-1,m,o+1)

""" The function `f4` takes three arguments: `n`, `m`, and `o`. Each time it calls itself recursively, it decrements `n` by 1 and either increments `m` or `o`.

The function makes two recursive calls for every non-terminal call, and thus has a branching factor of 2. Every level of recursion reduces `n` by 1.

Let's break down the number of calls:

1. For `n=1`, there are 2 calls.
2. For `n=2`, each of the original 2 calls branches out into 2 more calls, making a total of 4 calls.
3. For `n=3`, the 4 calls from the previous level branch out into 8 calls.
4. And so on...

For a given `n`, the total number of calls will be (2^n). This is because the function essentially explores all possible combinations of incrementing either `m` or `o` for the given number of times `n` decrements. The number of such combinations is equivalent to the number of paths in a binary tree of height `n`.

Therefore, the time complexity of the function `f4` is O(2^n). """

def f5(n):
    for i in range(0,n,2):
        print(i)  
    if n<=0:
        return 1
    else:
        return 1 + f5(n-5)

""" The function `f5(n)` can be analyzed for time complexity as follows:

1. The loop `for i in range(0,n,2):` runs for n/2 iterations since it's incrementing by 2 in each step. This gives a time complexity of O(n/2) which is O(n) for this loop.

2. After the loop, the function recursively calls itself with the value `n-5` if `n` is greater than 0.

The recursive nature of the function can be broken down as follows:
- The first call takes roughly n steps.
- The next recursive call takes roughly n-5 steps.
- The one after that takes roughly n-10 steps.
- ...
- Until `n <= 0`.

If you sum these up, you get:
n + (n-5) + (n-10) + ... + 5 + 0

The number of terms in the sum is approximately n/5 because you are decrementing `n` by 5 in each recursive call.

Therefore, the total number of steps is roughly proportional to:
(n/5) * (n/2)

This gives a time complexity of O(n^2).

Note: The base cases (`n<=0`) just return a constant value and have a time complexity of O(1), which does not dominate the overall complexity.

In conclusion, the time complexity of the given function `f5(n)` is O(n^2). """