a1 = int(input())
b1 = int(input())
c1 = int(input())

result = a1 * b1* c1
result = list(str(result))

for i in range(10):
    print(result.count(str(i)))
