def rotate(matrix): 
    #code here
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        start, end = 0, n - 1
        while start < end:
            matrix[start][i] , matrix[end][i] = matrix[end][i], matrix[start][i]
            start += 1
            end -= 1

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
