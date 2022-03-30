cnt=0
a = int(input())

def fun(str):
    arr = list(str)
    result=a
    arrset = list(set(arr))
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            pass
        elif arr[i] in arr[i+1:]:
            result-=1
            break
    print(result)



for i in range(a):
    word=input()
    fun(word)
    
