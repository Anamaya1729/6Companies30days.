#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        return self.recurcivePower(N,R) % 1000000007

    def recurcivePower(self,N,R):
        if R == 0:
            return 1
        result = self.power(N,R//2)
        result = (result * result ) % 1000000007
        if R % 2 == 0:
            return result
        return result * N

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
