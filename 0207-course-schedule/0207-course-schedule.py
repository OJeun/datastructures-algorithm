from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) # key: prerequisite, values: courses after take a prerequisite

        for prerequisite in prerequisites:
            # prerequisite = [0, 1]
            pre_course = prerequisite[1]
            course = prerequisite[0]

            graph[pre_course].append(course)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            visited.add(course)

            for next_course in graph[course]:    
                if dfs(next_course) == False:
                    return False

            visited.remove(course)
            return True
                

        for num in range(numCourses): 
            if num in graph and num not in visited:
                if dfs(num) == False:
                    return False
            
        return True


            
