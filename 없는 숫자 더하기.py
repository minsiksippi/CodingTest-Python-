def solution(numbers):
    answer = -1
    arr = [0,1,2,3,4,5,6,7,8,9]
    
    arr2=[i for i in arr if i not in numbers]
    answer = sum(arr2)
    return answer
