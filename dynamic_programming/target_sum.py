# Space Complexity = O(n)
# Time Complexity = O(2^n)

def find_target_sum_ways(nums, target):
    length_nums = len(nums)
    result = []
    exprs = ["."] * (length_nums * 2)

    
    def helper(index, curr, expression):
        
        # Base Case
        if index > length_nums - 1:
            if curr == target:
                convert_exprs_to_str = "".join(expression)
                result.append(convert_exprs_to_str)
                return
            else:
                return
        
        # Recursion
        # Plus
        expression[index * 2] = "+"
        expression[index * 2 + 1] = str(nums[index])
        helper(index + 1, curr + nums[index], expression)

        # Minus
        expression[index * 2] = "-"
        expression[index * 2 + 1] = str(nums[index])
        helper(index + 1, curr - nums[index], expression)

        return result
    
    return helper(0, 0, exprs)

def findTargetSumWays(nums, target):
    def helper(index, sum_nums):
        # Base case
        if index == len(nums):
            return 1 if sum_nums == target else 0
        
        # Recursive case: consider both adding and subtracting the current number
        positive = helper(index + 1, sum_nums + nums[index])
        negative = helper(index + 1, sum_nums - nums[index])
        
        return positive + negative
    
    return helper(0, 0)




