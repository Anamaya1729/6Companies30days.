class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected[0])
        amount_of_provinces = len(isConnected[0])
        count = 0
        
        def dfs_util(province):
            visited[province] = 1
            
            for j in range(amount_of_provinces):
                if isConnected[province][j] == 1 and visited[j] == 0:
                    dfs_util(j)
        
        for i in range(0, len(visited)):
            if visited[i] == 0:
                count += 1
                dfs_util(i)
                
        return count
