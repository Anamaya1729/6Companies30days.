class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		freq, queue, ans = [0]*26, [], ""
		for i in range(len(A)):
		    c = A[i]
		    freq[ord(c) - 97] += 1
		    if freq[ord(c) - 97] == 1:
		        queue.append(c)
		    else:
		        while queue and freq[ord(queue[0]) - 97] > 1:
		            queue.pop(0)
		    if queue:
		        ans += queue[0]
		    else:
		        ans += "#"
		
		return ans

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)
