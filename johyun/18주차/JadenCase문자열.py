def solution(s):
    strList = s.split(' ')
    print(strList)
    for i in range(len(strList)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고 두번째 문자부터는 자동으로 소문자로
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        strList[i]=strList[i].capitalize()
        answer = " ".join(strList)
    return answer
