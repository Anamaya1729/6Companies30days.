class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cur = colors[0]
        count = 1
        hm = collections.defaultdict(int)
        for c in colors[1:]:
            if c == cur:
                count += 1
            else:
                if count > 2:
                    hm[cur] += count - 2
                count = 1
                cur = c
        if count > 2:
            hm[cur] += count - 2
        return hm['A'] > hm['B']
