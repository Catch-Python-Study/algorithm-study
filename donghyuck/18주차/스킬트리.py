def solution(skill, skill_trees):
    skill = list(skill)
    array = []
    for i in skill_trees:
        array.append(list(i))
    answer = 0
    for i in array:
        temp = []
        cnt = 0
        for j in skill:

            if j in i:
                temp.append(i.index(j))
            else:
                temp.append(100+cnt)
            cnt += 1

            if cnt >= 2:
                if temp[cnt-1] <= temp[cnt-2]:
                    temp.pop()
                    break
        if len(temp)==len(skill):
            answer += 1
    return answer