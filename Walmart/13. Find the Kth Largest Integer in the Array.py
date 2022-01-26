class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(i) for i in nums]
        return str(sorted(nums, reverse = True)[k-1])
