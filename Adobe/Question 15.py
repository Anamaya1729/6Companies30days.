class Solution:
    def nextPermutation(self, N, arr):
        i = N-1
        while i > 0:
            if arr[i] > arr[i-1]:
                arr[i:N] = sorted(arr[i:N])
                for j in range(i,N):
                    if arr[j] > arr[i-1]:
                        arr[j],arr[i-1] = arr[i-1],arr[j]
                        return arr
            i-=1
        return arr[::-1]
        

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
