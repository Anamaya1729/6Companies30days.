import sys

class Solution:
    name = "A"
    answer = ""
    
    def matrixChainOrder(self, Pvalues, n):
        m = [[0 for x in range(n)] for y in range(n)]
        bracket = [[0 for x in range(n)] for y in range(n)]
        
        for i in range(n):
            m[i][i] = 0
            
        for l in range(2,n):
            for i in range(1,n-l+1):
                j = i + l - 1
                m[i][j] = sys.maxsize
                
                for k in range(i,j):
                    q= m[i][k] + m[k+1][j] + (Pvalues[i-1] * Pvalues[k] * Pvalues[j])
    
                    if q < m[i][j]:
                        m[i][j] = q
                        bracket[i][j] = k
        self.name = "A"
        self.answer = ""
        self.printParenthesis(1,n-1,bracket)
        return self.answer
        
    def printParenthesis(self,i,j,bracket):
        if i == j:
            self.answer += self.name
            self.name = chr(ord(self.name) + 1)
            return
        else:
            self.answer += "("
            self.printParenthesis(i,bracket[i][j], bracket)
            self.printParenthesis(bracket[i][j] + 1, j ,bracket)
            self.answer += ")"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = input().split()
        for i in range(n):
            p[i] = int(p[i])
        
        ob = Solution()
        print(ob.matrixChainOrder(p, n))
