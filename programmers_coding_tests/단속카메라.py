def solution(routes):
    """
    1. 진출점 순서대로 정렬
    2. for loop 카메라 위치와 진입점을 비교
    3. i의 진입점이 카메라 현재 위치보다 크면 i의 진출점을 새로운 카메라 위치로 지정
    """
    answer = 0

    # 진입점이 진출점보다 클 경우(역으로 갈경우) 체크를 위해 모든 진입/진출지점은 작은값에서 큰값으로 정렬
    for i in routes:
        i.sort()
    routes.sort(key=lambda x: x[1])

    tmp_r = float("-inf")
    for i in routes:
        if tmp_r < i[0]:
            tmp_r = i[1]
            answer += 1

    return answer


"""
[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	2
"""

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))