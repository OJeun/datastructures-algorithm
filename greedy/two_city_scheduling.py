# Time complexity = O(nlogn)
# Space Complexity = O(1)
def two_city_sched_cost(costs):
    sorted_costs = sorted(costs, key= lambda x: x[0]- x[1])
    num_of_ppl = len(costs)
    min_cost = 0


    for i in range(num_of_ppl):
        if i < (num_of_ppl // 2):
            min_cost += sorted_costs[i][0]
        else:
            min_cost += sorted_costs[i][1]

    return min_cost