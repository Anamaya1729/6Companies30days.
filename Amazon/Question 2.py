class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        
        up_count, down_count, i = 0, 0, 0
        res = 0
        while i < len(arr)-1:
            while i < len(arr)-1 and arr[i] == arr[i+1]:
                i +=1
            
            while i < len(arr)-1 and arr[i] < arr[i+1]:
                up_count += 1
                i += 1
            
            while i < len(arr)-1 and arr[i] > arr[i+1]:
                down_count += 1
                i += 1
            
            if up_count > 0 and down_count > 0:
                res = max(res, up_count+down_count+1)
            
            up_count = down_count = 0
                    
        return res
