# Space Complexity = O(1)
# time complexity = O(nlogn)
def fractionalknapsack(W,arr,n):
    # Sort arr by ratio profit / weight
    arr.sort(reverse=True, key= lambda x:x[0]/x[1]) # sort: O(nlogn) finding profit/weight = O(n)
    remaining_weight = W
    value = 0 

    for i in range(n):
        if remaining_weight == 0:
            break
        weight = min(remaining_weight, arr[i][1])
        remaining_weight -= weight
        value += (arr[i][0] / arr[i][1]) * weight

    return value


arr = [[70, 10], [90, 20], [150, 30]]
W= 25
n = len(arr)
print(fractionalknapsack(W, arr, n))