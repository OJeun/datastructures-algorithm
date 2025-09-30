class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        temp = 0
        time = 0

        # while loop while the number of the ticket at index k reaches 0
        while tickets[k] > 0:

            if tickets[temp] > 0:
                tickets[temp] -= 1
                time += 1

            temp += 1
            temp = temp % n

        return time
