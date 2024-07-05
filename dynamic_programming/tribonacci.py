def tribonacci(n):
    if n < 2:
        return n
    if n == 2:
       return 1
    first = 0
    second = 1
    curr = 1
    count = 1
    while count < n - 1:
        next = first + second + curr
        first = second
        second = curr
        curr = next

        count += 1
    return next

print(tribonacci(4))