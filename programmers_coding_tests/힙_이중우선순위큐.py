def solution(operations):
    queue = []
    for i in operations:
        # 큐 삽입
        if i[:2] == "I ":
            queue.append(int(i[2:]))
        # 최댓값 삭제
        elif i == "D 1" and queue:
            queue.remove(max(queue))
        # 최솟값 삭제
        elif i == "D -1" and queue:
            queue.remove(min(queue))

    return [max(queue), min(queue)] if queue else [0, 0]


"""
["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	[0,0]
["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	[333, -45]
"""
operations_list = [
    ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
    ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
]
for operations in operations_list:
    print(solution(operations))
