import math


def solution(n, stations, w):
    answer = 0
    start = 1  # 출발점
    cal = 2 * w + 1
    # 이미 설치된 기지국 기준 설치되지 않은 범위 구하기
    for i in stations:
        end = i - w - 1

        # (현재 구간의 길이 / 전파길이) 올림처리한 값이 기지국 갯수
        answer += math.ceil((end - start + 1) / cal)

        # 시작점 갱신
        start = i + w + 1

    # stations가 오름차순이니 지금 체크하는값이 마지막 값이면서 갱신된 시작점이 최댓값보다 작을경우 더 지을게 남아있음.
    # 마지막의 시작점부터 끝까지의 기지국 갯수 체크
    if start <= n:
        answer += math.ceil((n - start + 1) / cal)

    return answer


"""
N   statuons    W   answer
11	[4, 11]	    1	3
16	[9]	        2	3
"""

input_list = [
    [11, [4, 11], 1],
    [16, [9], 2]
]

for i in input_list:
    print(solution(i[0], i[1], i[2]))
