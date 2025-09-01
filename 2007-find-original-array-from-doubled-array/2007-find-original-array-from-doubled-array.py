class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        result = []

        if len(changed)%2 != 0:
            return result
        
        changed.sort()

        frequency = dict()

        for num in changed:
            frequency[num] = frequency.get(num, 0) + 1

        for num in changed:
            
            while frequency.get(num) > 0:
                if not frequency.get(num*2):
                    return []
                frequency.get(num*2)
                frequency[num] -= 1
                frequency[num*2] -= 1
                result.append(num)

        return result