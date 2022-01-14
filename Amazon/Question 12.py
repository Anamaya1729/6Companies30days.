class Solution:
    def colName (self, n):
        # your code here
        ans = ""
        while n:
            n-= 1
            rem = n % 26
            ans = chr(ord("A") + rem) + ans
            n = n// 26
        return ans
t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
