#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        N = len(arr)
        s = set()
        arr.sort()
        for i in range(N-3):
            for j in range(i + 1, N-2):
                lo = j + 1
                hi = N-1
                while lo < hi:
                    summ = arr[i] + arr[j]+ arr[lo] + arr[hi]
                    if summ == k:
                        s.add((arr[i],arr[j], arr[lo],arr[hi]))
                        lo += 1
                        hi -= 1
                    elif summ > k:
                        hi -= 1
                    else:
                        lo += 1
        return sorted(list(s))
                            
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends
