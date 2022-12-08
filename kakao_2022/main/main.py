from library.common import GameMatchingRequester, PlayerInfo
from config.settings import PROBLEM


def game_matching(matching_cls):
    player_cls = PlayerInfo()

    # game play
    for game_time in range(595):
        waiting_player = matching_cls.waiting_api_call()
        game_result = matching_cls.game_result_api_call()
        print('time: [{0}]'.format(game_time), waiting_player)

        for game_rs in game_result:
            if PROBLEM == 2 and game_rs.get('taken') <= 10:
                continue
            player_cls.calc_player_mmr(game_rs)

        waiting_player = sorted(waiting_player, key=lambda x: x['from'] - game_time)

        pairs = []
        matched = set()
        # 기다린 시간: 실력차 허용치
        allowed_range = {5: 0.1, 10: 0.2, 15: 0.3}
        for idx, user1 in enumerate(waiting_player):
            if user1.get('id') in matched:
                continue

            allowed = allowed_range[5]
            for wait, value in allowed_range.items():
                if user1.get('from') - game_time <= wait:
                    allowed = value
                    break

            another_user = None
            for idx2 in range(idx + 1, len(waiting_player)):
                user2 = waiting_player[idx2]
                if user2.get('id') in matched or idx == idx2:
                    continue

                diff = abs(player_cls.win_rate(user1.get('id'), user2.get('id')) - 0.5)
                if diff <= allowed:
                    another_user = user2
                    break

            if another_user:
                # print(f'{user_power[user1.id]} {user_power[another_user.id]} {win_rate(user1.id, another_user.id)}')
                pairs.append([user1.get('id'), another_user.get('id')])
                matched.add(user1.get('id'))
                matched.add(another_user.get('id'))

        if game_time == 594:
            # 점수순서대로 정렬
            players = dict(sorted(player_cls.get_all_player().items(), key=lambda x: x[1], reverse=True))
            commands = []
            for idx, player_id in enumerate(players):
                commands.append({'id': player_id, 'grade': 9999 - idx})
            matching_cls.change_grade_api_call(commands)

        matching_cls.match_api_call(pairs)
    # 종료
    matching_cls.match_api_call()

    print(player_cls.get_all_player())
    print(matching_cls.user_info_api_call())


if __name__ == '__main__':
    matching_cls = GameMatchingRequester()
    game_matching(matching_cls)

    print(matching_cls.score_api_call())
