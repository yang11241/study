def solution(triangle):
    dt_list = []  # 모든 경로를 지났을 때 생성 될 최댓값 리스트
    for i, k in enumerate(triangle):
        # 첫번째는 1개뿐이니깐 그냥 리스트에 추가
        if i == 0:
            dt_list.append(k[0])
        # 두번째는 2개라서 첫번째와 합이 최댓값.
        elif i == 1:
            dt_list.append([triangle[i - 1][0] + k[0], triangle[i - 1][0] + k[1]])
        # 그 이후는 양끝 제외하고 사이에 있는 값들은 두개의 경로가 있어 둘 중 큰값으로 넣어주면 됨.
        else:
            tmp_list = []
            for i2, k2 in enumerate(k):
                # 맨 왼쪽
                if i2 == 0:
                    tmp_list.append(dt_list[-1][0] + k2)
                # 맨 오른쪽
                elif i2 == i:
                    tmp_list.append(dt_list[-1][-1] + k2)
                # 그 사이
                else:
                    tmp_list.append(max(dt_list[-1][i2 - 1] + k2, dt_list[-1][i2] + k2))
            dt_list.append(tmp_list)
    return max(dt_list[-1])  # 맨 마지막줄의 최댓값이 구하고자하는 값


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # result 30
