res = -1


def solution(begin, target, words, chk_word='', d=0, visit=[]):
    global res

    if target not in words:
        return 0

    if chk_word == '':
        chk_word = begin

    if chk_word == target:
        res = d if res == -1 else min(res, d)
        return

    for word in words:
        chk_cnt = 0
        for s1, s2 in zip(chk_word, word):
            if s1 != s2:
                chk_cnt += 1

        if chk_cnt == 1 and word not in visit:
            tmp_d = d + 1
            visit.append(word)
            solution(begin, target, words, word, tmp_d, visit)
            visit.remove(word)

    return res


"""
begin   target  words                                       return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	        0
"""

input_list = [
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]
]

for i in input_list:
    print(solution(i[0], i[1], i[2]))
