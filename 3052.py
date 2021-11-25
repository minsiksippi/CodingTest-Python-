arr = []
result = []
cnt = 0

for i in range(10):
    arr.append(int(input()))

for j in range(10):
    result.append(arr[j]%42)

result = set(result)
print(len(result))
