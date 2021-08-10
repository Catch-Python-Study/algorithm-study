import re
import collections
def solution(str1, str2):
    
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-z|A-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-z|A-Z]+', str2[i:i+2])]
    
    
    # print(str1, str2)
    
    # 자카드 유사도 -> 합집합 교집합
    
    # 합집합과 교집합 계산 
    intersection_set = set(str1) & set(str2)
    union_set = set(str1) | set(str2)
    
    
    print(str1, str2, intersection_set, union_set)

    if len(union_set) == 0:
        return 65536

    # 교집합하고 합집합의 counter를 따로 계산
    
    intersectionSet_sum = sum([min(str1.count(i), str2.count(i)) for i in intersection_set])
    unionSet_sum = sum([max(str1.count(i), str2.count(i)) for i in union_set])
    
    print(intersectionSet_sum, unionSet_sum)
    
    return int((intersectionSet_sum / unionSet_sum) * 65536)