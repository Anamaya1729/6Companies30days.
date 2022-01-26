class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total, count, l = sum(piles), 0, len(piles)
        times , temp= l // 2, 1
        for i in reversed(range(times)):
            count += max(piles[i], piles[i + temp])
            temp  += 2
        if count > total // 2:
            return True
        return False
