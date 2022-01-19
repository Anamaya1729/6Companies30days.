from bisect import bisect_left

class Solution:
    def minInsAndDel(self, A, B, N, M):
        # code here 
        vec = []
        s = set(B)
        for i in A:
            if i in s:
                vec.append(i)
        res = self.LongestIncreasingSubsequenceLength(vec)
        return abs(N - res) + abs(M - res)
        
    def LongestIncreasingSubsequenceLength(self,v):
        if len(v) == 0:
            return 0
     
        tail = [0 for i in range(len(v) + 1)]
        length = 1
     
        tail[0] = v[0]
     
        for i in range(1, len(v)):
            if v[i] > tail[length-1]:
                tail[length] = v[i]
                length += 1
     
            else:
                tail[bisect_left(tail, v[i], 0, length-1)] = v[i]
     
        return length


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minInsAndDel(A,B,N,M))
