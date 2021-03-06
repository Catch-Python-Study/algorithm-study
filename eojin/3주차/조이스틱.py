def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    print(make_name)

    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) ==0:
            break
        left, right = 1, 1
        while make_name[idx - left] ==0:
            left +=1
        while make_name[idx + right] ==0:
            right +=1

        if left<right:
            answer+=left
            idx += -left
        else:
            answer+=right
            idx += right

    return answer

print(solution("JEROEN"))