def solve(a):
    return sum(a)

n = int(input())
arr = []
for i in range(n):
    arr.append(i+1)

print(solve(arr))
