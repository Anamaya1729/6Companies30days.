
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        arr_set = set(arr)
        repeated_num = sum(arr) - sum(arr_set)
        missing_num = abs(sum(arr_set) - n*(n+1)//2)
        return repeated_num, missing_num



if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
