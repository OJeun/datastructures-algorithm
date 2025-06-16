class Solution:
    def calcEquation(self, equations, values, queries) -> list[float]:
        graph = defaultdict(dict)
        result = []

        # fill up the two-way graph
        for index in range(len(equations)):
            equation = equations[index]
            value = values[index]

            numerator = equation[0]
            denumerator = equation[1]

            graph[numerator][denumerator] = value
            graph[denumerator][numerator] = 1/value

        def dfs_iteration(start, target):
            if start not in graph or target not in graph:
                return -1

            stack = [(start, 1)]
            visited = set()
            
            while stack:
                prev = stack.pop()
                for neighbor, weight in graph[prev[0]].items():
                    acc_value = prev[1] * weight
                    if neighbor == target:
                        return acc_value
                    if neighbor not in visited:
                        stack.append((neighbor, acc_value))
                        visited.add(neighbor)
            
            return -1

        def dfs_recursion(curr, target, acc):
            if curr not in graph or target not in graph:
                return -1
            
            visited.add(curr)

            for neighbor, weight in graph[curr].items():
                if neighbor == target:
                    return acc * weight
                if neighbor not in visited:
                    dfs_result = dfs_recursion(neighbor, target, acc*weight)
                    if dfs_result is not None:
                        return dfs_result

                

        for query in queries:
            numerator = query[0]
            denumerator = query[1]
            visited = set()
            result.append(dfs_recursion(numerator, denumerator, 1))

        return result