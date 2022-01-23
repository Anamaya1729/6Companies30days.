class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
      
        
        start = max(weights) - 1
        end = sum(weights)
        
        while end - start > 1: 
            m = (end + start)//2
            if self.solve(m, weights) <= days:
                end = m
            else: 
                start = m
                
        return end
    
    def solve(self, capacity, weights):
        prev = 0 
        ans = 0 
        for num in weights: 
            prev += num
            if prev > capacity: 
                ans += 1
                prev = num

        return ans + 1 if prev > 0 else ans
