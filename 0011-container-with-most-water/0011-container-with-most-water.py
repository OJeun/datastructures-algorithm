class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        start = 0
        end = len(height) - 1

        while start < end:
                max_water = max(max_water, (end - start) * min(height[end], height[start]))
                
                if height[start] > height[end]:
                    end -= 1
                else:
                    start += 1
                    
        
        return max_water 