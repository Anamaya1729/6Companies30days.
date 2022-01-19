class Solution:
    M = 1000000007
    dp = [[0 for _ in range(1001)] for k in range(1001)]
    
    def kvowelwords(self, N,K):
		for i in range(N+1):
		    for j in range(K+1):
		        self.dp[i][j] = -1
		return self.solve(N, 0, K) % self.M

    def solve(self, n, count, k):
        if n== 0:
            return 1
        if self.dp[n][count] != -1:
            return self.dp[n][count] % self.M
        if count == k:
            self.dp[n][count] = ((21%self.M)* (self.solve(n-1, 0, k))%self.M) % self.M
            return self.dp[n][count]
        self.dp[n][count] = (((21 % self.M) * (self.solve(n-1, 0, k))%self.M)%self.M + (5*(self.solve(n-1, count + 1, k))%self.M)%self.M)%self.M        
        return self.dp[n][count]


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,K = map(int,input().split())
		ob = Solution()
		ans = ob.kvowelwords(N,K)
		print(ans)
# } Driver Code Ends
