def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)
        print(skill_list, skills)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
