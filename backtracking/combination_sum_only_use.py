# Space Complexity = O(n)
# Time Complexity = O(2^n)
def combination_sum_only_use_element(candidates, target):
    output = []
    candidates.sort() # O(n)
    len_candidates = len(candidates)
    
    def helper(index, curr_sum, curr):
        if curr_sum == target:
            output.append(curr[:])
            return
        if curr_sum > target:
            return
        if index == len_candidates:
            return
        hash_map = {}
        for j in range(index, len_candidates):
            element = candidates[j]
            if element not in hash_map:
                hash_map[element] = True
                curr.append(element)
                helper(j+1, curr_sum + element, curr)
                curr.pop()
            
    helper(0, 0, [])
    return output
        