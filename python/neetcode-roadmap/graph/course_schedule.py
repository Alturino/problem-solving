from collections import deque
from typing import List


# DFS
class Solution:
    # DFS
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

    # # BFS
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     courseToPrerequisites = {i: [] for i in range(numCourses)}
    #     indegree = [0] * numCourses
    #     for course, prerequisite in prerequisites:
    #         courseToPrerequisites[course].append(prerequisite)
    #         indegree[prerequisite] += 1
    #
    #     q = deque()
    #     for i in range(numCourses):
    #         if indegree[i] == 0:
    #             q.append(i)
    #
    #     visited = 0
    #     while q:
    #         course = q.popleft()
    #         visited += 1
    #
    #         for prerequisite in courseToPrerequisites[course]:
    #             indegree[prerequisite] -= 1
    #             if indegree[prerequisite] == 0:
    #                 q.append(prerequisite)
    #
    #     return numCourses == visited
