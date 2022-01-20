def convertor(n):
    s = ""
    for i in range(31, -1, -1):
        j = n >> i
        if j & 1 == 1:
            s+= "1"
        else:
            s+= "0"
    for i in range(32):
        if s[i] == "1":
            return s[i:]

def generate(N):
    ans = []
    for i in range(1, N + 1):
        tempString = convertor(i)
        ans.append(tempString)
    return ans

import atexit
import io
import sys


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
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
# } Driver Code Ends
