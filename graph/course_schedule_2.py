from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseToPrerequisites = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            if course in courseToPrerequisites:
                courseToPrerequisites[course].append(prerequisite)

        result = []
        visited, cycle = set(), set()

        def isCycleAndTopologicalSortWithReference(course: int) -> bool:
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prerequisite in courseToPrerequisites[course]:
                if isCycleAndTopologicalSortWithReference(prerequisite) == False:
                    return False
            cycle.remove(course)

            visited.add(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if isCycleAndTopologicalSortWithReference(course) == False:
                return []

        return result


# s = Solution()
# print(s.findOrder(2, [[1, 0]]))


s = Solution()
print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
