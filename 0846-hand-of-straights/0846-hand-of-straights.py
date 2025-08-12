import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        frequency = dict()

        for num in hand:
            frequency[num] = frequency.get(num, 0) + 1

        heapq.heapify(hand)
        minH = hand

        while minH:
            min_val = heapq.heappop(minH)
            if frequency.get(min_val):
                frequency[min_val] -= 1
                for i in range(1, groupSize):
                    sequence = min_val + i
                    count = frequency.get(sequence)
                    if count and count > 0:
                        frequency[sequence] -= 1
                    else:
                        return False

        return True