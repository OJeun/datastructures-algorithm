from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courses = defaultdict(list)
        self.visited = set()
        self.valid_courses = set()

        for second, first in prerequisites:
            courses[second].append(first)

        # To detect any cycle in a graph
        def is_cycle(course):
            if course in self.valid_courses:
                return False

            if course in self.visited:
                return True

            self.visited.add(course)

            for prerequisite in courses.get(course, []):
                if is_cycle(prerequisite) == True:
                    return True

            self.valid_courses.add(course)
            self.visited.pop()

            return False

        for course in range(numCourses):
            if course not in self.valid_courses:
                if is_cycle(course) == True:
                    return False

        return True