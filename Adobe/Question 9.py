
class Solution:
    def nextPalin(self,N):
        st, n = str(N), len(str(N))
        if n <= 3:
            return "-1"
        half = st[:n//2]
        half = list(half)
        if self.next_permutation(half):
            half = "".join(half)
            ans = half
            if n & 1:
                ans += s[n//2]
            half = half[::-1]
            ans += half
            return ans
        return "-1"
            
    def next_permutation(self,a):
        for i in reversed(range(len(a) - 1)):
            if a[i] < a[i + 1]:
                break
        else:  
            return False  

        j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])
        a[i], a[j] = a[j], a[i]
        a[i + 1:] = reversed(a[i + 1:])
        return True


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.nextPalin(s))
