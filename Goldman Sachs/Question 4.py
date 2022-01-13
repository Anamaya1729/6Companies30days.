def encode(arr):
    # Code here
    res = []
    arr = list(arr)
    last_str = ""
    for i in arr:
        if i != last_str:
            last_str = i
            res.append(i)
            res.append("1")
        else:
            res[-1] = str(int(res[-1]) + 1)
    return "".join(res)
            
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
