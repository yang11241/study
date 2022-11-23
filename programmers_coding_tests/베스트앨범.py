def solution(genres, plays):
    answer = []  # return
    tmp_list = {}  # 임시 저장 dict
    play_time = {}  # 총 재생횟수

    # {genres: [{idx: plays}, {idx: plays}]} 형태로 정리
    # 해당 장르의 총 재생횟수 계산 - {genres: 총 재생횟수} 형태
    for idx, val in enumerate(genres):
        if val in tmp_list:
            tmp_list[val].append({'idx': idx, 'plays': plays[idx]})
            play_time[val] += plays[idx]
        else:
            tmp_list[val] = [{'idx': idx, 'plays': plays[idx]}]
            play_time[val] = plays[idx]

    # 해당 장르의 재생횟수 내림차순으로 정렬, 최대 2개까지만 다시 정리
    for k, v in tmp_list.items():
        tmp_list[k] = sorted(v, key=lambda k: k['plays'], reverse=True)[:2]

    # 재생횟수 내림차순 정렬
    max_play_list = sorted(play_time.items(), key=lambda k: k[1], reverse=True)

    # 재생횟수가 많은거부터 return 배열에 고유번호 i 담기
    for i in max_play_list:
        for j in tmp_list[i[0]]:
            answer.append(j['idx'])

    return answer


"""
genres                                          plays                       return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
"""

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))