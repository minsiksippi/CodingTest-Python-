n, x = input().split()
n = int(n)
x = int(x)
arr = list(map(int, input().split()))
    
for i in range(n):
    if arr[i]<x:
        print(arr[i], end = " ")
