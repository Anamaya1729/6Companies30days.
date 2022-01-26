class Solution:
    def find3number(self,A, n):
        # code here
        stack, result = [], []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= A[i]:
                stack.pop()
            stack.append(A[i])
            if len(stack) == 3:
                break
        if len(stack) >= 3:
            for i in range(2, -1, -1):
                result.append(stack.pop())
        return result



import sys
sys.setrecursionlimit(100000)

def isSubSeq(arr, lis, n, m):
    if m==0:
        return True
    if n==0:
        return False
    if arr[n-1]==lis[m-1]:
        return isSubSeq(arr, lis, n-1, m-1)
    return isSubSeq(arr, lis, n-1, m)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    lis = Solution().find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis)!=0 and len(lis)!=3:
        print(-1)
        continue
    if len(lis)==0:
        print(0)
    elif lis[0]<lis[1] and lis[1]<lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)
        
# } Driver Code Ends
