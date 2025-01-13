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

# Time Complexity = O(2^2n)
# Space Complexity = O(2n)
def two_city_sched_cost_recursive(costs):
    n = len(costs)
    half_of_ppl = n // 2

    def helper(index, a_city, b_city):
        # Base Case
        if index > n - 1:
            return 0
        
        city_a_cost = city_b_cost = float('inf')
        # Recursive Case
        for i in range(index, n):
            # Choose city A
            if a_city > 0:
                city_a_cost = costs[i][0] + helper(i+1, a_city-1, b_city)

            # Choose city B
            if b_city > 0:
                city_b_cost = costs[i][1] + helper(i+1, a_city, b_city-1)
            
            return min(city_a_cost, city_b_cost)

    return helper(0, half_of_ppl, half_of_ppl)

# Time Complexity = O(n^2)
# Space Complexity = O(n^2)
def two_city_sched_cost_memoization(costs):
    n = len(costs)
    half_of_ppl = n // 2
    # key: num of A city, value: minimum cost
    dp = {}

    def helper(index, a_city, b_city):
        if (index, a_city) in dp:
            return dp[(index, a_city)]
        
        # Base Case
        if index > n - 1:
            return 0
        
        city_a_cost = city_b_cost = float('inf')
        # Recursive Case
        for i in range(index, n):
            # Choose city A
            if a_city > 0:
                city_a_cost = costs[i][0] + helper(i+1, a_city-1, b_city)

            # Choose city B
            if b_city > 0:
                city_b_cost = costs[i][1] + helper(i+1, a_city, b_city-1)
            
            dp[(index, a_city)] = min(city_a_cost, city_b_cost)
            return dp[(index, a_city)]

    return helper(0, half_of_ppl, half_of_ppl)

# Space Complexity = O(n^2)
# Time Complexity = O(n^2)
def two_city_sched_cost_tabulation(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs) // 2
    dp = [[float('inf')] * (n + 1) for _ in range(2*n + 1)]
    dp[0][0] = 0
    
    for i in range(1, 2*n + 1):
        for j in range(max(0, i - n), min(n, i) + 1):
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + costs[i-1][0])
            if j < i:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + costs[i-1][1])
                
    return dp[2*n][n]


