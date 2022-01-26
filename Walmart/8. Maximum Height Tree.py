class Solution:
    def height(self, N):
        # code here
        i, rem = 1, 1
        while rem <= N:
            rem += i + 1
            i += 1
        return i - 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.height(N))
