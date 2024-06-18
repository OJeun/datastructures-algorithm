# space complexity: O(n)
# time complexity: O(2^n)
# T(n) = 2T(n-1) + 1
def toh(N, fromm, to, aux):
    count = 0
    def helper(N, fromm, to, aux):
        nonlocal count
        if N == 1:
            print("Move disk", N, "from rod", fromm, "to", to)
            count += 1
            return
        helper(N-1, fromm, aux, to)
        print("Move disk", N - 1, "from rod", fromm, "to", aux)
        count += 1
        helper(N-1, aux, to, fromm)
    helper(N, fromm, to, aux)
    return count
