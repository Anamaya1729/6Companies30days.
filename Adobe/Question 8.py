class Solution:

    def atoi(self,string):
        temp = list(string)
        if temp[0] =="-":
            temp = temp[1:]
        for i in temp:
            try:
                if int(i):
                    continue
            except ValueError:
                return -1
        return int(string)

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
