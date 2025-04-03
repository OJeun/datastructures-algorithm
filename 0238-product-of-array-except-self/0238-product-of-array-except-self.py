class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = 1
        product = [1]

        # fill product list, if i = 2, proudct[i] = product of elements that are less than index 2.
        for i in range(1, len(nums)):
            product.append(product[i - 1] * nums[i - 1])
        for j in range(len(nums) - 2, -1, -1):
            right_product *= nums[j + 1]
            product[j] = product[j] * right_product

        return product
