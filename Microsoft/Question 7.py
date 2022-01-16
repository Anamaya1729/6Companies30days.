class Solution:
	def findMaxArea(self, grid):
		#Code here
		max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_area = max(self.areaCount(grid,i,j),max_area)
        return max_area
		
	def areaCount(self,grid, x, y):
	    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
	        return 0
	    if not grid[x][y]:
	        return 0
	    grid[x][y] = 0
	    return 1 + self.areaCount(grid, x - 1, y) + self.areaCount(grid, x + 1, y) + self.areaCount(grid, x , y - 1) + self.areaCount(grid, x , y + 1) + self.areaCount(grid, x , y - 1) + self.areaCount(grid, x - 1, y - 1) + self.areaCount(grid, x + 1, y + 1) + self.areaCount(grid, x + 1, y - 1) + self.areaCount(grid, x - 1, y + 1)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.findMaxArea(grid)
		print(ans)
