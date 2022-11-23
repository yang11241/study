def solution(n, works):
    if sum(works) <= n:
        return 0

    for i in range(n):
        works[works.index(max(works))] -= 1

    answer = sum([i * i for i in works])

    return answer


"""
works       n   result
[4, 3, 3]	4	12
[2, 1, 2]	1	6
[1,1]	3	0
"""
input_list = [
    [[4, 3, 3], 4],
    [[2, 1, 2], 1],
    [[1, 1], 3]
]
for i in input_list:
    print(solution(i[1], i[0]))
