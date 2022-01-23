"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        
        def getVal(sum, n):
            if sum == 0:
                return 0
            elif sum == n*n:
                return 1
            else:
                return 2
        
        cumsum = copy.deepcopy(grid)
        
        nrows = len(grid)
        ncols = len(grid[0])
        
        for r in range(nrows):
            for c in range(ncols):
                if r == 0 and c == 0:
                    pass
                elif r == 0:
                    cumsum[r][c] = cumsum[r][c-1] + grid[r][c]
                elif c == 0:
                    cumsum[r][c] = cumsum[r-1][c] + grid[r][c]
                else:
                    cumsum[r][c] = cumsum[r][c-1] + cumsum[r-1][c] - cumsum[r-1][c-1] + grid[r][c]
        
        def getSum(left, right, top, bottom):
            
            ans = cumsum[bottom][right]
            if left - 1 >= 0:
                ans -= cumsum[bottom][left-1]
            if top - 1 >= 0:
                ans -= cumsum[top-1][right]
            if left - 1 >= 0 and top - 1 >= 0:
                ans += cumsum[top-1][left-1]
            return ans
            
        def recurse(left, right, top, bottom):
            
            n = right - left + 1
            if n == 1:
                return Node(grid[top][left], True, None, None, None, None)
                
            rowMid = (top+bottom)//2
            colMid = (left+right)//2
            
            topLeftSum = getSum(left, colMid, top, rowMid)
            topLeftVal = getVal(topLeftSum, n//2)                
            topRightSum = getSum(colMid+1, right, top, rowMid)
            topRightVal = getVal(topRightSum, n//2)
            bottomLeftSum = getSum(left, colMid, rowMid+1, bottom)
            bottomLeftVal = getVal(bottomLeftSum, n//2)
            bottomRightSum = getSum(colMid+1, right, rowMid+1, bottom)
            bottomRightVal = getVal(bottomRightSum, n//2)
            
            if (topLeftVal, topRightVal, bottomLeftVal, bottomRightVal) == (0,0,0,0):
                return Node(0, True, None, None, None, None)
                
            elif (topLeftVal, topRightVal, bottomLeftVal, bottomRightVal) == (1,1,1,1):
                return Node(1, True, None, None, None, None)
            else:
                head = Node(1, False, None, None, None, None)
                head.topLeft = recurse(left, colMid, top, rowMid)
                head.topRight = recurse(colMid+1, right, top, rowMid)
                head.bottomLeft = recurse(left, colMid, rowMid+1, bottom)
                head.bottomRight = recurse(colMid+1, right, rowMid+1, bottom)
                return head
            
        return recurse(0, ncols-1, 0, nrows-1)   
