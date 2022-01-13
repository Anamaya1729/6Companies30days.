class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        string, i, j, count = "", 0, 0, 1
        while i <= len(S):
            if i == len(S) or S[i] == "I":
                while count >= 1:
                    if count <= j: 
                        break
                    string += str(count) 
                    count -= 1
                j = i + 1
                count = i + 1
            count += 1
            i += 1
        return string
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
