# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

    
    
        

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lo, hi = 0, mountain_arr.length()-1
        while lo<hi:
            peak=lo+(hi-lo)//2
            if mountain_arr.get(peak)>mountain_arr.get(peak+1):
                hi = peak
            else:
                lo = peak + 1
        try1= self.binarySearch(mountain_arr, lo, target, True)
        try2 = self.binarySearch(mountain_arr, lo, target, False)
        if try1!=-1:
            return try1
        if try2!=-1:
            return try2
        return -1
                
    def binarySearch(self,mountain_arr, peak, target, before):
            if before:
                start, end = 0, peak
            else:
                start, end = peak, mountain_arr.length()-1
            
            while start<=end:
                mid = int(start + (end-start)/2)
                if mountain_arr.get(mid)==target:
                    return mid
                if before:
                    if target<mountain_arr.get(mid):
                        end=mid-1
                    else:
                        start = mid + 1
                else:
                    if target>mountain_arr.get(mid):
                        end=mid-1
                    else:
                        start = mid + 1
                    
            return -1
        
       
        
