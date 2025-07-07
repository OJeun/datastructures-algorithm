class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize empty stack to store indices of previous days
        previous_days = [0]
        # Initialize a result list to all 0 and named days
        days = [0] * len(temperatures)

        # loop through each index and temperature in temperatures
        for curr_index in range(1, len(temperatures)):
            # while stack is not empty current temp is larger than the temp on the top of stack
            while previous_days and temperatures[curr_index] > temperatures[previous_days[-1]]:
                # pop the top day index from stack
                recent_day = previous_days.pop()
                # find gap(curr_index - index stored on top)
                gap = curr_index - recent_day
                #  store that gaps into days list
                days[recent_day] = gap

            # push the curr index to stack
            previous_days.append(curr_index)

        # return days list
        return days
