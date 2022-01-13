class Solution:
    def squaresInChessBoard(self, N):
        squares = 0
        for i in range(1,N+1):
            squares += i**2
        return squares
             
             
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.squaresInChessBoard(N))
