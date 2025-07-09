class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:     
        # define fleets and initialize it to 0
        fleets = 1
        # pair a position of a car and its speed in a tuple and update position to that tuple
        for index in range(len(position)):
            pair = (position[index], speed[index])
            position[index] = pair

        # sort the position list by position
        position.sort(reverse=True)
        # define a time list initializing it to empty list
        time = []

        # iterate position list
        for index in range(len(position)):
            pos, speed = position[index]
            # calculate the time needed to get to the target from the position
            time_to_destination = (target - pos) / speed
            time.append(time_to_destination)

        # iterate time as long as the index is in bound, starting from 1
        index = 0
        while index < len(time) - 1:
            # while current time is larger than or equal to previous time
            merged = time[index]
            while index < len(time) - 1 and merged >= time[index + 1]:
                index += 1
            
            if index != len(time) - 1:
                fleets += 1
            index += 1

        return fleets