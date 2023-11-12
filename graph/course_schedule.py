from collections import deque
from typing import List


# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrerequisites = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            if course in courseToPrerequisites:
                courseToPrerequisites[course].append(prerequisite)

        visited = set()

        def dfs(course: int) -> bool:
            if course in visited:
                return False
            if course in courseToPrerequisites and courseToPrerequisites[course] == []:
                return True
            visited.add(course)

            for courseAsPrerequiste in courseToPrerequisites[course]:
                if not dfs(courseAsPrerequiste):
                    return False
            visited.clear()
            courseToPrerequisites[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
