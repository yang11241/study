def solution(n, s):
    # ex) 3, 8 >> [2, 3 ,3] - 모든 배열의 숫자가 차이가 제일 적어야 곱이 최대가 됨
    # 3, 8일 경우 div = 2, mod = 2 > div 한번, div + 1이 2번 > div는 n - mod번, div + 1은 mod번
    answer = []
    div = s // n  # 몫
    mod = s % n  # 나머지

    if not div:
        return [-1]

    for i in range(n - mod):
        answer.append(div)

    for i in range(mod):
        answer.append(div + 1)

    return answer


"""
n   s   result
2	9	[4, 5]
2	1	[-1]
2	8	[4, 4]
"""

input_list = [
    [2, 9],
    [2, 1],
    [2, 8]
]

for input in input_list:
    print(solution(input[0], input[1]))
