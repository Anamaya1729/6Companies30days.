class Solution:
    def calculateSpan(self,a,n):
        #code here
        span, stack = [0 for _ in range(n)], [0]
        span[0] = 1
        for i in range(1,n):
            span[i]  = 1
            j = i -1
            while j >= 0:
                if a[j] > a[i]:
                    break
                span[i] += span[j]
                j -= span[j]
        return span
            

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        print(*ans)
