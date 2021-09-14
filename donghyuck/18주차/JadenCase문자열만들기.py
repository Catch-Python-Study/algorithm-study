def solution(s):
    arr = s.split()
    answer = []
    
    for i in arr:
        change = i[0].upper() + i[1:].lower()
        answer.append(change)

    answer = ' '.join(answer)
    return answer