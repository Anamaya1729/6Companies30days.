#User function Template for python3

class Solution:
    def minSteps(self, D):
        # code here
        steps, summ = 0 , 0
        while True:
            summ += steps
            steps += 1
            if summ == D:
                return steps - 1
            if summ > D and (summ - D) % 2 == 0:
                return steps - 1
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        D = int(input())
        
        ob = Solution()
        print(ob.minSteps(D))
# } Driver Code Ends
