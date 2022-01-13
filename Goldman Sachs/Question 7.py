
class Solution:
    def findPosition(self, n , m , k):
        if m <= n - k + 1: return m + k - 1
        m = m - (n - k + 1)
        if m % n == 0: return n
        return m % n
 

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M,K=map(int,input().split())
        
        ob = Solution()
        print(ob.findPosition(N,M,K))
