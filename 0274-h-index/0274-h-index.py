class Solution:
    def hIndex(self, citations: List[int]) -> int:
        acc = 0
        count = [0] * (len(citations) + 1)

        for citation in citations:
            if citation >= len(citations):
                count[-1] += 1
            else:
                count[citation] += 1

        for i in range(len(citations), -1, -1):
            if count[i] >= i:
                return i
            else:
                acc += count[i]
            
            if acc >= i:
                return i

        
        