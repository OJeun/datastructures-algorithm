# Memorization
def fibonacci_memorization(n, ht={0:0, 1:1}):
    if n in ht:
        return ht[n] 
        
    else:
        ht[n] = fibonacci_memorization(n-1) + fibonacci_memorization(n-2)
        return ht[n]
    
# Tabulation
# Time complexity = O(n)
# Space complexity = O(n)
def fibonacci_tabulation(n, arr=[0,1]):
    # if n == 5, [0, 1, 1, 2, 3, 5]
    if n < 2:
        return arr[n]
    for i in range(2, n+1):
        ith_fib = arr[i-1] + arr[i-2]
        arr.append(ith_fib)
    return arr[n]

# Space optimized tabulation
# Time complexity = O(n)
# Space complexity = O(1)
def fibonacci_space_optimized_tabulation(n):
    # if n == 5, [0, 1, 1, 2, 3, 5]
    if n < 2:
        return n
    
    prev = 0
    curr = 1
    next = 0
    
    count = 1
    while count < n:
        next = prev + curr
        prev = curr
        curr = next
        count += 1

    return next

print(fibonacci_space_optimized_tabulation(5))