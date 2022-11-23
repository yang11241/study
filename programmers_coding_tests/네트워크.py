# Breath First Search (너비 우선 탐색, BFS)
def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


# Depth First Search (깊이 우선 탐색, DFS)
def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


def solution(n, computers):
    answer = 0
    graph = {}

    # dfs돌리기 위한 그래프의 형태 만들어주기
    for i in range(n):
        tmp_list = []
        for j in range(n):
            if computers[i][j] == 1:
                tmp_list.append(j)
        graph[i] = tmp_list

    # dfs를 컴퓨터의 개수만큼 돌려서 dfs의 리스트 길이가 1이면 독립적인 네트워크
    # dfs의 리스트 길이가 1이 아니면 연결된 다른 컴퓨터와 연결된 네트워크로 볼수있음
    # 서로 연결되어 있으면 dfs의 리스트 길이가 동일.
    tmp_set = set()
    for i in range(n):
        tmp_len = len(dfs(graph, i))
        if tmp_len == 1:
            answer += 1
        else:
            tmp_set.add(tmp_len)
    answer += len(tmp_set)
    return answer


"""
n   computers                           return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
"""

input_list = [
    [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]],
    [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]
]
for i in input_list:
    print(solution(i[0], i[1]))