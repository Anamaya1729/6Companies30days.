class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh_count = 0
        nums_of_orange = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh_count+=1
                    
        size = len(queue)
        if size == 0:
            return -1 if fresh_count > 0 else 0
        
        
        time = -1
        while queue:
            
            while size > 0:
                curr = queue.pop(0)
                size-=1
                
                if curr[0]>0 and grid[curr[0]-1][curr[1]] == 1:
                    queue.append([curr[0]-1,curr[1]])
                    grid[curr[0]-1][curr[1]] = 2
                    fresh_count-=1
                if curr[0] < len(grid)-1 and grid[curr[0]+1][curr[1]] == 1:
                    queue.append([curr[0]+1,curr[1]])
                    grid[curr[0]+1][curr[1]] = 2
                    fresh_count-=1
                if curr[1] > 0 and grid[curr[0]][curr[1]-1] == 1:
                    queue.append([curr[0],curr[1]-1])
                    grid[curr[0]][curr[1]-1] = 2
                    fresh_count-=1
                if curr[1] < len(grid[0])-1 and grid[curr[0]][curr[1]+1] == 1:
                    queue.append([curr[0],curr[1]+1])
                    grid[curr[0]][curr[1]+1] = 2
                    fresh_count-=1
                    
                    
            size = len(queue)
            time+=1
            

        return time if fresh_count == 0 else -1
        
