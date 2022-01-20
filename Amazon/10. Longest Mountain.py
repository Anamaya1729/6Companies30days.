class Solution:

	def matchPairs(self,nuts, bolts, n):
		nuts_hash = {}
		for i,v in enumerate(nuts):
		    nuts_hash[v] = i
		    
		bolts_hash = {}
		for i,v in enumerate(bolts):
		    bolts_hash[v] = i
		    
		i = 0
		for c in '!#$%&*@^~':
		    if nuts_hash.get(c)!=None and bolts_hash.get(c)!=None:
		        nuts[i] = c
		        bolts[i] = c
		        i += 1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1
