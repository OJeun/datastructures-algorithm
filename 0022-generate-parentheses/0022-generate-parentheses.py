class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol, res = [], []
        def helper(left, right):
            if left < right or left > n:
                return 

            if right == n:
                combination = "".join(sol)
                res.append(combination)
                return 
            
            # left parenthesis
            sol.append("(")
            helper(left+1, right)
            sol.pop()

            sol.append(")")
            helper(left, right+1)
            sol.pop()

        helper(0, 0)
        return res
            
