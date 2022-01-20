#User function Template for python3
import sys
class Solution:
    def maxProfit(self, k, n, prices):
        profit = [[0 for i in range(n + 1)] for j in range(k+1)]

        for i in range(1, k+1):
            prevDiff = float("-inf")
            for j in range(1,n):
                prevDiff = max(prevDiff, profit[i-1][j-1] - prices[j-1])
                profit[i][j] = max(profit[i][j - 1], prices[j] + prevDiff)
        
        return profit[k][n-1]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
