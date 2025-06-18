class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # Sort the points by Xfirst
        points.sort(key=lambda x: x[0])  # O(nlogn)

        number_of_balloons = len(points)
        boundary = points[0][1]
        spot = points[0][0] # where the arrow should go to
        arrows = 1

        for index in range(1, number_of_balloons):
            start, end = points[index]
            if start <= boundary:
                boundary = min(boundary, end)
                
            if start > boundary:
                arrows += 1
                boundary = end

        return arrows