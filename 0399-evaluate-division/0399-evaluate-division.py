from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()
        graph = defaultdict(list)
        queries_result = []

        for (f, t), value in zip(equations, values):
            graph[f].append((t, value))
            graph[t].append((f, 1/value))

        def dfs(f, t, visited, acc):
            visited.add(f)
            if f == t:
                return acc
            for connected_node in graph[f]:
                if connected_node[0] not in visited:     
                    new_acc = acc * connected_node[1]
                    result = dfs(connected_node[0], t, visited, new_acc)
                    if result != -1:
                        return result 
            return -1 
           

        for query in queries:
            numerator = query[0]
            denominator = query[1]
            if numerator not in graph or denominator not in graph:
                queries_result.append(-1.0)
            else:
                visited = set()
                queries_result.append(dfs(numerator, denominator, visited, 1))

        return queries_result
