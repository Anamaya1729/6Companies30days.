class Solution:
    def isValid(self, mat):
        # code here
        rowCheck = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        colCheck = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        gridCheck = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                check = mat[i][j]
                if check != 0:
                    if check in rowCheck[i] or check in colCheck[j]:
                        return 0
                    rowCheck[i].append(check)
                    colCheck[j].append(check)
                    
                    grid = (i//3)*3 + (j//3)
                    
                    if check in gridCheck[grid]:
                        return 0
                    gridCheck[grid].append(check)
        return 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
