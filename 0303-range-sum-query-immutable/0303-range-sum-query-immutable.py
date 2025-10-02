class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.accSum = self.getAcc()
        self.reverseAccSum = self.getReverseAcc()
        self.total = self.accSum[len(nums) - 1]

    def getAcc(self):
        output = []
        acc = 0
        for num in self.nums:
            acc += num
            output.append(acc)
        return output

    def getReverseAcc(self):
        reverse_sum = [0] * len(self.nums)
        acc = 0
        for i in range(len(self.nums) -1, -1, -1):
            acc += self.nums[i]
            reverse_sum[i] = acc
        return reverse_sum

    def sumRange(self, left: int, right: int) -> int:
        if left == right:
            return self.nums[left]
        if left - 1 < 0:
            return self.accSum[right]
        if right == len(self.nums) - 1:
            return self.reverseAccSum[left]

        return self.total - self.accSum[left - 1] - self.reverseAccSum[right + 1]