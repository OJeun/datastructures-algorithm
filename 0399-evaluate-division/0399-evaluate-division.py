from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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
                        stack.append((neighbor, prev[1] * weight))
                        visited.add(neighbor)
            
            return -1
                

        for query in queries:
            numerator = query[0]
            denumerator = query[1]

            result.append(dfs_iteration(numerator, denumerator))

        return result
                





                


                    
