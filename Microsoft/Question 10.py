class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        include, exclude = a[0], 0
        new_exclude = -1
        for i in range(1,n):
            if include > exclude:
                new_exclude = include
            else:
                new_exclude = exclude
            include = exclude + a[i]
            exclude = new_exclude
        if include > exclude:
            return include
        return exclude

import atexit
import io
import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
