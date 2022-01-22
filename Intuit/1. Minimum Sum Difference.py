#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
		total = sum(arr)
		temp = 0
		if total % 2 != 0:
		    temp = 1
		total = total // 2
		dp = [[0 for _ in range(total+1)] for _ in range(n + 1)]
		for i in range(1,n+1):
		    for j in range(1,total + 1):
		        if arr[i - 1] <= j:
		            dp[i][j] = max(arr[i-1] + dp[i - 1][j - arr[i - 1]], dp[i - 1][j])
		        else:
		            dp[i][j] = dp[i-1][j]
		ans = dp[n][total]
		return (2* total+ temp - ans) - ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)
