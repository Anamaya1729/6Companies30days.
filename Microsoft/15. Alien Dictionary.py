#User function Template for python3

class Solution:
    def findOrder(self,dicte, N, K):
        adj = [[] for _ in range(K)]
        for i in range(1, N):
            s1  = dicte[i - 1]
            s2 = dicte[i]
            for j in range(min(len(s1), len(s2))):
                if s1[j] != s2[j]:
                    u,v = ord(s1[j]) - ord("a"), ord(s2[j]) - ord("a")
                    adj[u].append(v)
                    break
                
        visited, topo = [0 for _ in range(K)], []
        for i in range(K):
            if not visited[i]:
                self.solve(i,visited, topo, adj)
        
        topo.reverse()
        s = ""
        for i in range(len(topo)):
            s += chr(topo[i] + ord("a"))
        return s
        
    def solve(self,src, visited, topo, adj):
        visited[src]  = 1
        for i in adj[src]:
            if not visited[i]:
                self.solve(i, visited,topo, adj)
        topo.append(src)
        
class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
