class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        count = 0
        prev_interval = intervals[0]
        n = len(intervals)

        for i in range(1, n):
            curr_interval = intervals[i]

            if prev_interval[1] > curr_interval[0]:
                count += 1
                if prev_interval[1] > curr_interval[1]:
                    prev_interval = curr_interval
            else:
                prev_interval = curr_interval

        return count