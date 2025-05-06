class Solution:
    def bubbleSort(self, nums):
        # Compare ith and (i+1)th element
        for j in range(len(nums) - 1, 0, -1):
            for i in range(0, j): 
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

    def selectionSort(self, nums):
        for i in range(len(nums) - 1): # 0 - 5
            min_index = i
            for j in range(i + 1, len(nums)): # 0 - 5
                if nums[j] < nums[min_index]:
                    min_index = j
            if min_index != i:
                nums[min_index], nums[i] = nums[i], nums[min_index]

        return nums

    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            current = nums[i]

            while i > 0 and nums[i-1] > nums[i]:
                nums[i] = nums[i-1]
                nums[i-1] = current
                i -= 1

        return nums

    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums

        half_index = len(nums) // 2

        sorted_first_half = self.mergeSort(nums[:half_index])
        sorted_second_half = self.mergeSort(nums[half_index:])

        new_list = []
        i = 0
        j = 0

        while i <= len(sorted_first_half) - 1 and j <= len(sorted_second_half) - 1:
            if sorted_first_half[i] <= sorted_second_half[j]:
                new_list.append(sorted_first_half[i])
                i += 1
            else:
                new_list.append(sorted_second_half[j])
                j += 1
        
        while i < len(sorted_first_half):
            new_list.append(sorted_first_half[i])
            i+=1

        while j < len(sorted_second_half):
            new_list.append(sorted_second_half[j])
            j+=1

        return new_list


     
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)


                

                



