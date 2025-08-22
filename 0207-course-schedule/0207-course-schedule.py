from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courses = defaultdict(list)
        self.visited = set()
        self.valid_courses = set()

        for second, first in prerequisites:
            courses[second].append(first)

        # To detect any cycle in a graph
        def dfs(course):
            if course in self.valid_courses:
                return False
                
            if course not in courses:
                self.valid_courses.add(course)
                return False

            if course in self.visited:
                return True

            self.visited.add(course)

            for prerequisite in courses[course]:
                is_cycle = dfs(prerequisite)
                
                if is_cycle == True:
                    return True

            self.valid_courses.add(course)

            return False

        for course in range(numCourses):
            if course not in self.valid_courses:
                if dfs(course) == True:
                    return False

        return True