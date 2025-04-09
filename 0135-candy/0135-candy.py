class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)
        total = 0

        # From left to right
        for i in range(len(ratings)- 1):
            if ratings[i] < ratings[i+1] :
                candies[i+1] = candies[i]+1

        # From right to left
        for j in range(len(ratings) - 1, 0, -1):
            if ratings[j] < ratings[j - 1]:
                candies[j - 1] = max(candies[j-1], candies[j] + 1)
        
        for candy in candies:
            total += candy

        return total

