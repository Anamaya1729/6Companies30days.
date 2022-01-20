from collections import defaultdict

class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        g = Graph(N)
        for edge in prerequisites:
            g.addEdge(edge[0],edge[1])
        if g.topologicalSort():
            return True
        return False
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) 
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def topologicalSort(self):
        in_degree = [0]*(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        cnt = 0
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u)
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
 
            cnt += 1
        if cnt != self.V:
            return False
        else :
            return True

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
