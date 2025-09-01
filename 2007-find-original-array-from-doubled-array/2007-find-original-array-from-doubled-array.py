class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        result = []

        if len(changed)%2 != 0:
            return result
        
        changed.sort()

        frequency = dict()

        for num in changed:
            frequency[num] = frequency.get(num, 0) + 1

        for num in changed:
            count = frequency.get(num)
            doubled = frequency.get(num*2)

            if count != 0:
                if doubled:
                    frequency[num] -= 1
                    frequency[num*2] -= 1
                    result.append(num)
                else:
                    return []

        return result
                