def solution(n, edge):
    # 노드별 연결된 모든 정보를 정리
    edge.sort()  # 1번노드부터 정리하기 위한 정렬
    graph_set = {i + 1: [] for i in range(n)}  # {n번노드 : 연결된 노드 리스트}
    node_length = {i + 1: 0 for i in range(n)}  # 1번부터 n번노드의 총 거리
    for i in edge:
        # 양방향노드라서 양쪽정보 다 넣어줌
        graph_set[i[0]].append(i[1])
        graph_set[i[1]].append(i[0])

    # 1번노드부터 체크하면서 거리 계산 시작함
    chk_node = [1]

    # 1번노드는 체크할 필요없으니 아래조건 안걸리게 그냥 1로 셋팅
    # 어차피 가장 멀리 떨어진거 구하는거라 상관없음
    node_length[1] = 1
    while chk_node:
        # 지금 가장앞에있는 노드번호를 꺼내기
        now_node = chk_node[0]
        del (chk_node[0])

        # 해당 노드와 간선으로 연결된 노드들을 찾아줌
        for i in graph_set[now_node]:
            # 연결된 노드의 1번부터 총 거리가 아직 셋팅되지 않았다면
            if node_length[i] == 0:
                # 다음에 체크할 노드로 연결된 노드값을 넣어주고
                # now_node의 1번부터 총 거리 + 1을 셋팅되지 않은 노드의 1번부터 총거리로 만들어줌
                chk_node.append(i)
                node_length[i] = node_length[now_node] + 1

    # node_length의 values들 중 max값을 가지는 key 갯수가 1번 노드에서 가장 멀리떨어진 노드들의 수
    return list(node_length.values()).count(max(node_length.items(), key=lambda k: k[1])[1])


"""
n   vertex                                                      return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
"""

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
