class Solution:
    def AllParenthesis(self,n):
        res = []
        s = ""
        self.solve(s, n, n, res)
        return res
        
    def solve(self, s, l, r, result):
        if l == 0 and r == 0:
            result.append(s)
            return
        elif l < 0 or r < 0:
            return
        self.solve(s + "(", l - 1, r,result )
        if l < r:
            self.solve(s + ")", l, r - 1, result)


if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
