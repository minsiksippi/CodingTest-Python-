def solution(lottos, win_nums):
    answer = []
    cnt = 0
    cnt_0 = 0
    for i in range(len(lottos)):
        if lottos[i]==0:
            cnt_0 = cnt_0 + 1
        for j in range(len(win_nums)):
            if lottos[i]==win_nums[j]:
                cnt=cnt+1
    if cnt == 6:
        answer.append(1)
        answer.append(1)
    elif cnt == 5:
        if cnt_0 == 1:
            answer.append(1)
        else:
            answer.append(2)
        answer.append(2)
    elif cnt ==4:
        
        if cnt_0 == 1:
            answer.append(2)
        elif cnt_0 == 2:
            answer.append(1)
        else :
            answer.append(3)
        answer.append(3)
    elif cnt == 3:
        if cnt_0 == 1:
            answer.append(3)
        elif cnt_0 == 2:
            answer.append(2)
        elif cnt_0 == 3:
            answer.append(1)
        else:
            answer.append(4)
        answer.append(4)
    elif cnt == 2:
        if cnt_0 == 1:
            answer.append(4)
        elif cnt_0 == 2:
            answer.append(3)
        elif cnt_0 == 3:
            answer.append(2)
        elif cnt_0 == 4:
            answer.append(1)
        else:
            answer.append(5)
        answer.append(5)
    elif cnt == 1:
        if cnt_0 == 1:
            answer.append(5)
        elif cnt_0 == 2:
            answer.append(4)
        elif cnt_0 == 3:
            answer.append(3)
        elif cnt_0 == 4:
            answer.append(2)
        elif cnt_0 == 5:
            answer.append(1)
        else:
            answer.append(6)
        answer.append(6)
    else :
        if cnt_0 == 1:
            answer.append(6)
        elif cnt_0 == 2:
            answer.append(5)
        elif cnt_0 == 3:
            answer.append(4)
        elif cnt_0 == 4:
            answer.append(3)
        elif cnt_0 == 5:
            answer.append(2)
        elif cnt_0 == 6:
            answer.append(1)
        else:
            answer.append(6)
        answer.append(6)
    return answer
