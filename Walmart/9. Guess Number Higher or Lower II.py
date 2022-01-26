class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            res = float('inf')
            for k in range(i, j + 1):
                res = min(res, max(dfs(i, k - 1), dfs(k + 1, j)) + k)
            return res
        res = dfs(1, n)
        dfs.cache_clear()
        return res
