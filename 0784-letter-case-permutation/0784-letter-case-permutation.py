class Solution:

    def letterCasePermutation(self, s: str) -> list[str]:
        permutations = []

        def permutation(index, perm: list):
            if len(perm) == len(s):
                str_perm = "".join(perm)
                permutations.append(str_perm)
                return

            char = s[index]
            if char.isdigit():
                perm.append(char)
                permutation(index+1, perm)
                perm.pop()

            if char.isalpha():
                perm.append(char)
                permutation(index+1, perm)
                perm.pop()

                char = s[index].lower() if s[index].isupper() else s[index].upper()
                perm.append(char)
                permutation(index+1, perm)
                perm.pop()
   
        

        permutation(0, [])
        return permutations