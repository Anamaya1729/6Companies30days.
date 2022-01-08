class Solution:
    
    def countSubArrayProductLessThanK(self, a, n, k):
        product , ans, start, end = 1, 0 , 0, 0
        while end < n:
            product *= a[end]
            while start<n and product >=k:
                product /= a[start]
                start +=1
            if product < k:
                ans += end - start + 1
                end += 1
        return ans
                
def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()
