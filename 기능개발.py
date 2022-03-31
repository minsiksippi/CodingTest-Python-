import math
from collections import Counter

def solution(progresses, speeds):
    answer = []
    arr=[]
    max = math.ceil((100-progresses[0])/speeds[0])
    for i in range(0, len(progresses)):
        if max >= math.ceil((100-progresses[i])/speeds[i]):
            arr.append(max)
        else:
            arr.append(math.ceil((100-progresses[i])/speeds[i]))
            max=math.ceil((100-progresses[i])/speeds[i])
        
    lista = Counter(arr)
    answer = (list(lista.values()))
    
    
                   
    return answer
