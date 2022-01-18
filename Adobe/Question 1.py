class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        low, high, summ, i = 0, n - 1, 0, 0
        try:
            while low <= high:
                summ += arr[i]
                if summ == s:
                    return [low + 1, i + 1]
                if summ > s:
                    while summ > s:
                        summ -= arr[low]
                        low += 1
                        if summ == s:
                            return [low + 1, i + 1]
                i += 1
        except IndexError:
                return [-1]
        return [-1]

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
