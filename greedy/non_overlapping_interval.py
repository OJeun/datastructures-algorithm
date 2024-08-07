# Time complexity = O(n)
def erase_overlap_intervals(intervals):
    n = len(intervals)
    count = 0
    i = 0
    while i < n-1:
        if intervals[i][1] < intervals[i+1][0]:
            i+=1
        else:
            count += 1
            if intervals[i][1] < intervals[i+1][1]:
                i += 2
            else:
                i += 1
    return count

# Time Complexity = O(nlogn)
def erase_overlap_intervals_2(intervals):
    intervals.sort(key=lambda x: x[1])
    removal_count = 0
    last_end = float('-inf')
    
    for start, end in intervals:
        if start >= last_end:
            last_end = end
        else:
            removal_count += 1
    
    return removal_count