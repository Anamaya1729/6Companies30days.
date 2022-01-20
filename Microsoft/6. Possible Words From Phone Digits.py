class Solution:
    def possibleWords(self,a,N):
        ans = []
        if N == 0:
            return ans
        index, output, arr = 0, "", ["", "","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.solve(a,N,index,output,ans,arr)
        return ans
        
    def solve(self,digits, n, index, output,ans, arr):
        if index == n:
            ans.append(output)
            return
        digit = digits[index]
        temp = arr[digit]
        for i in range(len(temp)):
            output += temp[i]
            self.solve(digits, n, index + 1, output,ans, arr)
            output = output[:len(output) - 1]

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
