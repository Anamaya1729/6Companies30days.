import heapq

class Solution:
    def smallestRange(self, numbers, n, k):
        minheap=[]
        maxx=-float('inf')
        
        for i in range(k):
           heapq.heappush(minheap,(numbers[i][0],i,0))
           maxx=max(numbers[i][0],maxx)
           
        heapq.heapify(minheap)
        diff=maxx-minheap[0][0]
        ans=[minheap[0][0],maxx]
        
        while True:
            
           mini, r, c = heapq.heappop(minheap)
           if diff>maxx-mini:
               diff=maxx-mini
               ans=[mini,maxx]
               
           if c+1>=len(numbers[r]):
               break
           num=numbers[r][c+1]
           maxx=max(maxx,num)
           heapq.heappush(minheap,(num,r,c+1))
        return ans
        

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
