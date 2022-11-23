def solution(A, B):
    A.sort()
    B.sort()

    rs_list = []
    for i in B:
        # A > B를 만족하는 A의 원소들을 임시리스트에 담고
        tmp_list = []
        for j in A:
            if i > j:
                tmp_list.append(j)
                break;
        if tmp_list:
            # 임시리스트가 값을 들고있으면 최솟값을 A에서 제거해주기
            A.remove(min(tmp_list))

        # rs_list에 담아주기 즉, rs_list는 B의 각 index에 위치한 사람이 이길수 있는 경우의 수를 나타냄
        rs_list.append(tmp_list)

    return len([1 for i in rs_list if i])  # rs_list의 각 원소가 존재하면 B가 이길수 있는 애들


"""
A           B           result
[5,1,3,7]	[2,2,6,8]	3
[2,2,2,2]	[1,1,1,1]	0
"""

input_list = [
    [[5, 1, 3, 7], [2, 2, 6, 8]],
    [[2, 2, 2, 2], [1, 1, 1, 1]]
]

for i in input_list:
    print(solution(i[0], i[1]))
