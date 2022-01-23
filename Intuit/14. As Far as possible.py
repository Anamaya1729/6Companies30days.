class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols, d, step, ans = len(grid), len(grid[0]), [[0, 1], [0, -1], [-1, 0], [1, 0]], 0, 0
        visited = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j))
        def isValid(xx, yy):
            return xx >=0 and yy >=0 and xx < rows and yy < cols
        while len(q) > 0:
            s = len(q)
            step += 1 
            while s > 0:
                s = s - 1
                u, v = q.popleft()
                visited[u][v] = True
                for i in range(4):
                    xx, yy = d[i][0] + u, d[i][1] + v
                    if isValid(xx, yy) and visited[xx][yy] == False and grid[xx][yy] == 0:
                        grid[xx][yy] = step
                        ans = max(ans, step)
                        q.append((xx, yy))
        return ans if ans != 0 else -1
