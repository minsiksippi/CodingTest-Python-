def func(str1):
    score = 0
    num = 1
    if str1[0]=='O':
        score=1
    else:
        score=0
        
    for i in range(1,len(str1)):
        if str1[i-1]=='O' and str1[i]=='O':
            num=num+1
            score = score + num
        elif str1[i-1]=='O' and str1[i]=='X':
            num=1
        elif str1[i-1]=='X' and str1[i]=='O':
            num=1
            score = score + num



    print(score)

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
    func(arr[i])

