n = int(input())
arr = []
res = 0
arr = list(map(int, input().split()))

maxS = max(arr)

for i in range(n):
    arr[i] = float(float(arr[i])/maxS * 100)
    res = res + arr[i]

print(res/n)
