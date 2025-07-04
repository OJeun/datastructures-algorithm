class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        # merged # initialize with the first interval sublist
       

        # sort the intervals by starts
        intervals.sort(key=lambda interval: interval[0])
        merged = [intervals[0]]

        # loop through intervals starting from second interval
        for curr in range(1, len(intervals)):
            curr_interval = intervals[curr]
            prev_interval = merged[-1]
            
            # if merged[-1][1](end index of last interval) >= curr_interval[start] ==> overlap exists
                # merge two intervals 
            if prev_interval[1] >= curr_interval[0]:
                prev_interval[1] = max(prev_interval[1], curr_interval[1])
            else:
                merged.append(curr_interval)


        return merged
        # return merged