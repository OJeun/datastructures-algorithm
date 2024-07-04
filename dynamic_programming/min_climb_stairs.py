def min_cost_climbing_stairs(cost):
    
    def cost_from(index):
        if index > len(cost) - 1:
            return 0

        one_step = cost[index] + cost_from(index + 1)
        two_steps = cost[index] + cost_from(index + 2)

        return min(one_step, two_steps)

    return min(cost_from(0), cost_from(1))


min_cost_climbing_stairs([10, 20, 30])