class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        res = [] 
        sums.sort()
        
        while len(sums) > 1:
            num = sums[-1] - sums[-2]
            countMap = Counter(sums)
            excluding = [] 
            including = [] 
            
            for x in sums:
                if countMap.get(x) > 0:
                    excluding.append(x)
                    including.append(x+num)
                    countMap[x] -= 1
                    countMap[x+num] -= 1

            if 0 in excluding:
                sums = excluding
                res.append(num)
            else:
                sums = including
                res.append(-1*num)
        return res
