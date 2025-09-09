class Solution:

    def letterCasePermutation(self, s: str) -> list[str]:
        permutations = []
        n = len(s)
        path = list(s)

        def permutation(index):
            if index == n:
                permutations.append(''.join(path))
                return

            if s[index].isdigit():
                path[index] = s[index]
                permutation(index + 1)
            
            else: 
                path[index] = s[index].lower()
                permutation(index+1)
                path[index] = s[index].upper()
                permutation(index+1)
        
        permutation(0)
        return permutations