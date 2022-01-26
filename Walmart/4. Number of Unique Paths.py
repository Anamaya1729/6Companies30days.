class Solution:
    def NumberOfPaths(self,a, b):
        dp = [[0 for i in range(b)] for j in range(a)]
        for i in range(a):
            dp[i][0] = 1
        for i in range(b):
            dp[0][i] = 1
        for i in range(1,a):
            for j in range(1,b):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[a - 1][b - 1]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))
