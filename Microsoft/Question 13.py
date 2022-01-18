#User function Template for python3

class Solution:
   
    #Function to find if the given edge is a bridge in graph.
    vis = [0 for _ in range(100001)]
    def isBridge(self, V, adj, c, d):
        # code here
        for i in range(V):
            self.vis[i] = 0
        self.solve(c,adj,c,d)
        if not self.vis[d]:
            return 1
        return 0
        
    def solve(self, i, adj, c, d):
        self.vis[i]  = 1
    
        for x in adj[i]:
            if i == c and x == d:
                continue
            if not self.vis[x]:
                self.solve(x,adj, c, d)
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends
