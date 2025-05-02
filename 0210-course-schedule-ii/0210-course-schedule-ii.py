from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites_dict = defaultdict(list)
        schedule = []
        visiting = set()

        # key: next course, value: prerequisites
        for courses in prerequisites:
            prerequisite = courses[1]
            next_course = courses[0]
            prerequisites_dict[next_course].append(prerequisite)

        def cycle(course, track) -> bool:
            if course in track:
                return True
            if course in visiting:
                return False

            track.add(course)

            for next_course in prerequisites_dict[course]:
                if next_course not in visiting:
                    if cycle(next_course, track):
                        return True

            schedule.append(course)
            visiting.add(course)
            track.remove(course)

        for course in range(numCourses):
            if course not in prerequisites_dict:
                schedule.append(course)
                visiting.add(course)
            else:
                track = set()
                if course not in visiting and cycle(course, track):
                    return []

        return schedule
        