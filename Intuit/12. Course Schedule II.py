from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        indegree = [0]*numCourses
        for i in range(numCourses):
            for edge in graph[i]:
                indegree[edge] += 1

        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        if len(res) == numCourses:
            return res
        return []
