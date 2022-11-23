def solution(gems):
    cnt_gems_type = len(set(gems))
    if cnt_gems_type == 1:  # 보석 하나일때
        return [1, 1]
    elif cnt_gems_type == len(gems):  # 보석들의 수와 종류의 갯수가 동일한 경우
        return [1, len(gems)]
    else:
        # 그 외
        start, end = 0, 0  # 시작점, 끝점
        chk_set = {}  # 보석별 구매건수 체크 dict
        tmp_list = []  # 모든 보석을 구매하는 리스트의 리스트
        for gem in gems:
            if gem in chk_set:
                chk_set[gem] += 1
            else:
                chk_set[gem] = 1
            end += 1  # 모든 보석을 살때까지 종료지점 +1
            while len(chk_set) == cnt_gems_type:
                # gems를 시작부터 end까지 구매한 보석의 수를 하나씩 빼다가 0이되면 모든보석을 구매한게 아님
                # 해당 보석을 chk_set에서 아예 빼버리고 while 탈출
                # while 돌때동안 start + 1
                chk_set[gems[start]] -= 1
                if chk_set[gems[start]] == 0:
                    del chk_set[gems[start]]
                start += 1
                tmp_list.append([start, end])

    # 위에서 생성된 리스트에서 길이가 제일 짧고, 길이가 같으면 시작이 작은 리스트를 가져오기
    answer = sorted(tmp_list, key=lambda x: (x[1] - x[0], x[0]))[0]
    return answer


"""
gems                                                                result
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]
["AA", "AB", "AC", "AA", "AC"]	[1, 3]
["XYZ", "XYZ", "XYZ"]	[1, 1]
["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	[1, 5]
"""

input_list = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
]

for i in input_list:
    print(solution(i))
