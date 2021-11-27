cnt = 0
def func(n):
    global cnt    
    n=str(n)
    a1=int(n[0])
    a2=int(n[1])
    a3=int(n[2])
    
    if (a1-a2)==(a2-a3):
        cnt=cnt+1
        
n=int(input())

if n >= 100:
    for i in range(100,n+1):
        func(i)

    print(99+cnt)
    
else:
    print(n)
    

