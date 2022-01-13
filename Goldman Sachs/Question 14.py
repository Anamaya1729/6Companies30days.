class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        size = len(nums)
        currSum = 0  
        res = size+1  

        for r in range(size):  
            if nums[r] >= target:  
                return 1

            currSum += nums[r]

            while currSum >= target:  
                res = min(res, r-l+1)
                currSum, l = currSum - nums[l], l+1

        return res % (size+1)
