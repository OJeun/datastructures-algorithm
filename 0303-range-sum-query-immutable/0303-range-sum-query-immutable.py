class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefixSum = self.getAcc()

    def getAcc(self):
        output = []
        acc = 0
        for num in self.nums:
            acc += num
            output.append(acc)
        return output

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right] - self.prefixSum[left] + self.nums[left]

        