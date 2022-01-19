class Solution:
    def winner(self,arr,n):
        count = {}
        for i in arr:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
        
        max_votes = max(count.values())
        for i in sorted(count):
            if count[i] == max_votes:
                return [i, max_votes]

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
