from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_graph = defaultdict(list)
        visiting = set()

        for courses in prerequisites:
            prerequisite = courses[0]
            course = courses[1]
            prerequisites_graph[prerequisite].append(course)
        
        def cycle(course, tracker):
            if course in tracker:
                return True

            if course in visiting:
                return False

            tracker.add(course)
            
            for next_course in prerequisites_graph[course]:
                if cycle(next_course, tracker):
                    return True

            visiting.add(course)
            tracker.remove(course)
            return False

        for course in range(numCourses):
            tracker = set()
            if course not in visiting and cycle(course, tracker):
                return False

        return True