class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue_pacific = deque()
        queue_atlantic = deque()
        
        m, n = len(heights), len(heights[0])
        
        visited_pacific = [[False for i in range(n)] for j in range(m)]
        visited_atlantic = [[False for i in range(n)] for j in range(m)]
        
        for i in range(m):
            queue_pacific.append((i, 0))
            queue_atlantic.append((i, n - 1))
            
        for i in range(n):
            queue_pacific.append((0, i))
            queue_atlantic.append((m - 1, i))
            
        self.bfs(queue_pacific, visited_pacific, heights)
        self.bfs(queue_atlantic, visited_atlantic, heights)  
        
        result = []
        
        for i in range(m):
            
            for j in range(n):
                
                if visited_pacific[i][j] and visited_atlantic[i][j]:
                    result.append((i, j))
                    
        return result

    def bfs(self, queue, visited, heights):
        
        m, n = len(visited), len(visited[0])
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        while queue:
            
            i, j = queue.popleft()
            
            if visited[i][j]:
                continue
                
            visited[i][j] = True
            
            for k in range(4):
                
                ni = i + dx[k] 
                nj = j + dy[k]
                
                if ni >= 0 and ni < m and nj >= 0 and nj < n and not visited[ni][nj] and heights[ni][nj] >= heights[i][j]:
                    queue.append((ni, nj))
