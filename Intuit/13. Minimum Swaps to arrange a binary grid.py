class Solution:
     def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        arr = []
        S = set()
        for row in grid:
            c = 0
            for i in row[::-1]:
                if i:
                    break
                c += 1
            while c in S:
                c -= 1
            if c >= 0:
                S.add(c)
                arr += c,
            
        if len(arr) < n:
            return -1
        
        res = 0
        for i, v in enumerate(arr):
            for v2 in arr[i+1:]:
                if v2 > v:
                    res += 1
        return res
