"""Q: find max 10 numbers in a list having 10M entries.
  

Answer 1: If it is sorted in the descending order then the first 10 distinct numbers will be our answers. Its time complexity would be O(nlogn) if used merge sort.

Answer 2: It can also be solved in O(n) Time Complexity by just traversing the entries and having 10 variables. !st for maximum value and 2nd for seconde max and so on... 
For example, if you need to find second largest value we just have to check if it is smaller than largest but still bigger than all other entries."""

class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        return sorted(li, reverse = True)[:k]

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
