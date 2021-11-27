n = int(input())
m = str(input())

sum = 0
for i in range(n):
    m=int(m)
    sum = sum + m%10
    m=m//10

print(sum)
