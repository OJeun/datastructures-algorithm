# Time complexity = O(2^n)
# Space complexity = O(n)
def min_cost_climbing_stairs_recursive(cost):
    
    def cost_from(index):
        if index > len(cost) - 1:
            return 0

        one_step = cost[index] + cost_from(index + 1)
        two_steps = cost[index] + cost_from(index + 2)

        return min(one_step, two_steps)

    return min(cost_from(0), cost_from(1))

# Time complexity = O(n)
# Space complexity = O(n)
def min_cost_climbing_stairs_memoization(cost):
    min_cost = [-1] * len(cost)
    def cost_from(index):
        if index > len(cost) - 1:
            return 0
        
        if min_cost[index] != -1:
            return min_cost[index]
        
        one_step = cost[index] + cost_from(index + 1)
        two_steps = cost[index] + cost_from(index + 2)

        min_cost[index] = min(one_step, two_steps)
        return min_cost[index]

    return min(cost_from(0), cost_from(1))

# Time complexity = O(n)
# Space complexity = O(n)
def min_cost_climbing_stairs_tabulation(cost):
    num_of_stairs = len(cost)
    if num_of_stairs == 1:
        return cost[0]
    
    if num_of_stairs == 2:
        return min(cost[0], cost[1])
    
    



