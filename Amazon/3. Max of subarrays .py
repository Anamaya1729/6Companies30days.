
class Solution:
    def max_of_subarrays(self,arr,n,k):
        i, j, output, l = 0 , 0 , [], []
        
        while j < n:
            while l and l[-1] < arr[j]:
                l.pop()
            l.append(arr[j])
            if j-i +1 < k:
                j+= 1
            elif j - i + 1 == k:
                output.append(l[0])
                if arr[i] == l[0]:
                    l.pop(0)
                i+= 1
                j+= 1
        return output
            

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
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
