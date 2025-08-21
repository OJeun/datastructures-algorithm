class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        result = []
        flag = False

        if not intervals:
            return [newInterval]

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if end < new_start:
                result.append(interval)

            elif start > new_end:
                if flag == False:
                    result.append([new_start, new_end])
                    flag = True
                result.append(interval)

            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        if flag == False:
            result.append([new_start, new_end])

        return result

