a = input()
a=int(a)
n=1

for i in range(a):
    b,c = input().split()
    b=int(b)
    c=int(c)
    print("Case #",n,": ",b," + ",c, " = ",b+c, sep="")
    n=n+1
