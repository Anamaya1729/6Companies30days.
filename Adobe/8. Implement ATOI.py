class Solution:
    def atoi(self,string):
        negative = False
        if string[0] =="-":
            negative = True
            string = string[1:]
        ans = 0
        for i in range(len(string)):
            if ord(string[i]) >= ord("0") and ord(string[i]) <= ord("9"):
                ans = ans * 10 + (ord(string[i]) - ord("0"))
            else:
                return -1
        if negative:
            return 0 - ans
        return ans

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
