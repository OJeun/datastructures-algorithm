class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        frequency = dict()

        for num in hand:
            frequency[num] = frequency.get(num, 0) + 1

        hand.sort()

        for num in hand:
            if frequency.get(num):
                frequency[num] -= 1
                for i in range(1, groupSize):
                    sequence = num + i
                    count = frequency.get(sequence)
                    if count and count > 0:
                        frequency[sequence] -= 1
                    else:
                        return False

        return True