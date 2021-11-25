n = int(input())
arr = []
for i in range(n):
    sum=0
    avg=0
    cnt=0
    rate = 0.0
    arr = list(map(int, input().split()))
    for j in range(1, arr[0]+1):
        sum = sum + arr[j]
        avg = sum/arr[0]

    for k in range(1,arr[0]+1):
        if arr[k]>avg:
            cnt = cnt + 1
    rate = cnt/arr[0] * 100
    rate = "{:.3f}%".format(rate)
    print(rate)
