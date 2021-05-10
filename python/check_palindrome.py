def check_palindrome(string):
    element_count_dic = {}

    # 문자열에 속한 문자의 갯수를 딕셔너리에 저장
    for element in string:
        if element in element_count_dic:
            element_count_dic[element] += 1
        else:
            element_count_dic[element] = 1

    # 문자열의 길이가 짝수라면, 각 문자의 개수가 모두 짝수인지 확인
    if len(string) % 2 == 0:
        for element in element_count_dic:
            if element_count_dic[element] % 2 != 0:
                return False

    # 문자열의 길이가 홀수라면, 홀수인 원소가 하나만 존재하는 지 확인
    else:
        odd_count = 0

        for element in element_count_dic:
            if element_count_dic[element] % 2 != 0:
                odd_count += 1
                if odd_count > 1:
                    return False
    return True
