class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        result = []
        flag = False

        if not intervals:
            return [newInterval]

        for i in range(len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]

            if end < new_start:
                result.append(interval)

            elif start > new_end:
                result.append([new_start, new_end])
                return result + intervals[i:]

            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        result.append([new_start, new_end])
        return result



