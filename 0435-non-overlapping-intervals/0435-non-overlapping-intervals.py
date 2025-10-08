class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        count = 0
        l, r = 0, 1
        n = len(intervals)

        while r < n:
            first_interval = intervals[l]
            second_interval = intervals[r]

            first_end = first_interval[1]
            second_first = second_interval[0]

            if first_end > second_first:
                count += 1
                r += 1
            else:
                l = r
                r += 1

        return count
