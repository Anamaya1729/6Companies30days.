
class Solution:
	def CountWays(self, s):
		if s == '0':
            return 0
        n = len(s)    
        if n<=1:
            return 1        
        if s[0] == '0' or '00' in s:
            return 0    
        dp = [1 for _ in range(n+1)]    
        for i in range(2,n+1):
            (d1,d2) = (int(s[i-2]),int(s[i-1]))        
            if d1>0 and d2>0:
                if d1*10+d2 < 27:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if d1 == 0:
                    dp[i] = dp[i-1]
                else:
                    if d1 > 2:
                        return 0
                    else:
                        dp[i] = dp[i-2]
        return dp[-1]%(10**9 + 7)
      
import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)
