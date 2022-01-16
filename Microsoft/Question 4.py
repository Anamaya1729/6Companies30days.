class Solution:
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        ans = []
        rs, re, cs, ce, i = 0, r - 1, 0, c - 1, 0
        while rs <= re and cs <= ce:
            if i%2 == 0:
                for j in range(cs, ce+1):
                    ans.append(matrix[rs][j])
                rs+= 1
                
                
                for j in range(rs,re+1):
                    ans.append(matrix[j][ce])
                ce -=1
                
            else:
                for j in range(ce, cs-1,-1):
                    ans.append(matrix[re][j])
                re -= 1
                
                for j in range(re, rs-1, -1):
                    ans.append(matrix[j][cs])
                cs += 1
            i+= 1
        return ans
                    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()
