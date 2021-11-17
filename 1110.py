num = int(input())
num2 = num
new_num = num
count = 0
while 1:
    if new_num>=10:
        a = new_num//10
        b= new_num%10
        hap=(a+b)%10
    else:
        b=new_num
        hap = new_num

    new_num = b*10 + hap
    count = count + 1
    if num2 == new_num:
        break

print(count)
        
