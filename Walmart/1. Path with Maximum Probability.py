class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(set)
        
        for i in range(0, len(edges)):
            prob = succProb[i]
            a, b = edges[i]
            graph[a].add((b, prob))
            graph[b].add((a, prob))
        
        q = collections.deque()
        q.append((start, 1.0))
        
        used = defaultdict(float)
        used[start] = 1.0
        
        ans = 0
        while q:
            node, prob = q.popleft()
            if node == end:
                ans = max(ans, prob)
            for nxt, nxtProb in graph[node]:
                if used[nxt] < prob * nxtProb:
                    q.append((nxt, prob * nxtProb))
                    used[nxt] = prob * nxtProb
            
        return ans
