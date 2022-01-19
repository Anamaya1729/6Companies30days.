class Solution:
    def maxCoins(self,arr, n):
        dp = [[-1 for i in range(n+ 1)] for j in range(n + 1)]
        return self.solve(arr, 0, n-1, dp)
        
    def solve(self,array, start, end, dp):
        if(start==end):
            dp[start][end]=array[start]
            return array[start]
        elif(end==start+1):
            dp[start][end]=max(array[start],array[end])
            return dp[start][end]
        elif(dp[start][end]!=-1):
            return dp[start][end]
        else:
            first=array[start]+min(self.solve(array,start+2,end,dp),self.solve(array,start+1,end-1,dp))
            last=array[end]+min(self.solve(array,start+1,end-1,dp),self.solve(array,start,end-2,dp))
            dp[start][end]=max(first,last)
            return dp[start][end]
        

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
