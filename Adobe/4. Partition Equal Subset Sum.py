class Solution:
    def equalPartition(self, N, arr):
        # code here
        summ  = sum(arr)
        if summ % 2 != 0:
            return 0
        return self.solve(arr, summ//2, N)
        
    def solve(self, arr, summ, n):
        dp = [[0 for _ in range(summ+1)] for i in range(n + 1)]
        
        for i in range(n+1):
            for j in range(summ+1):
                if i == 0:
                    dp[i][j] = 0
                if j == 0:
                    dp[i][j] = 1
                    
        for i in range(1,n + 1):
            for j in range(1, summ + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = max(dp[i-1][j-arr[i-1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[n][summ]

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
