# Time complextiy = O(2^n)
# Space complexity = O(n)
def climb_stairs(n):
    #write code here
    #n>=1 
    if n < 3:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)

# Time complextiy = O(n)
# Space complexity = O(n)
def climb_stairs_memorization(n, dict={1: 1, 2: 2}):
    if n in dict:
        return dict[n]
    else:
        dict[n] = climb_stairs_memorization[n-1] + climb_stairs_memorization[n-2]
        return dict[n]
    
# Time complexity = O(n)
# Space complexity = O(n)
def climb_stairs_tabulation(n, arr=[1, 2]):
    if n < 3:
        arr[n-1]

    count = 2

    while count < n:
        next_step = arr[count - 1] + arr[count - 2]
        arr.append(next_step)

    return arr[n-1]
    
    return


# Time complexity = O(n)
# Space complexity = O(1)
def climb_stairs_optimized_tabulation(n):
    if n < 3:
        return n
    prev = 1
    curr = 2
    next = 0

    count = 1
    while count < n - 1:
        next = prev + curr
        prev = curr
        curr = next
        count += 1

    return next
