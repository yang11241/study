from library.common import *

if __name__ == '__main__':
    game_matching_class = GameMatchingRequester(problem=1)
    game_matching_class.match_api_call()    # 시간 1부터 매칭 시작
    waiting_list = game_matching_class.waiting_api_call()
    # match_list = []
    # pairs = []
    # for idx, waiting in enumerate(waiting_list):
    #     match_list.append(waiting['id'])
    #     if idx % 2 == 1:
    #         pairs.append(match_list)
    #         match_list = []
    # rs = game_matching_class.match_api_call(pairs=[[13, 17], [24, 4], [8, 14], [9, 2], [1, 7]])
    # print(rs, game_matching_class.waiting_api_call())