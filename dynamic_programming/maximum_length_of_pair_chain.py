def find_longest_chain_recursive(pairs):
    length = len(pairs)
    sorted_pairs = sorted(pairs, key=lambda x: x[0])

    def helper(curr, prev):
        if curr > length -1:
            return 0
            
        exclude = helper(curr + 1, prev)
        
        include = 0
        if prev == -1 or sorted_pairs[curr][0] > sorted_pairs[prev][1]:
            include = 1 + helper(curr + 1, curr)

        return max(exclude, include)
        
    return helper(0, -1)

pairs = [[4, 5],[2, 9],[1, 2]]
print(find_longest_chain(pairs))
