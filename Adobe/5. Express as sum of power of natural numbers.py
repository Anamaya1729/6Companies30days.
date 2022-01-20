

class Solution:
    def numOfWays(self, n, x):
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        M = (pow(10,9)) + 7
        for i in range(1,n+1):
            for j in range(n, i -1 , -1):
                y = pow(i,x)
                if j >= y:
                    dp[j] = (dp[j] + dp[j - y]) % M
        return dp[n]


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,x = input().split()
		n=int(n)
		x=int(x)
		ob = Solution();
		print(ob.numOfWays(n, x))
