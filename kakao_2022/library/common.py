import json
import requests

from config.settings import *


class GameMatchingRequester(object):

    def __init__(self):
        self.auth_key = None
        self.problem = PROBLEM
        self.base_url = BASE_URL
        self.x_auth_token = X_AUTH_TOKEN
        self.start_app_call()

    def start_app_call(self):
        headers = {
            'X-Auth-Token': self.x_auth_token,
            'Content-Type': 'application/json'
        }
        data = {'problem': self.problem}
        rs_data = self.requests_call_func(method='POST', url=self.base_url + '/start', headers=headers, data=data)
        self.auth_key = rs_data.get('auth_key')

    def waiting_api_call(self):
        rs_data = self.requests_call_func(method='GET', url=self.base_url + '/waiting_line')
        return rs_data.get('waiting_line')

    def game_result_api_call(self):
        rs_data = self.requests_call_func(method='GET', url=self.base_url + '/game_result')
        return rs_data.get('game_result')

    def user_info_api_call(self):
        rs_data = self.requests_call_func(method='GET', url=self.base_url + '/user_info')
        return rs_data.get('user_info')

    def match_api_call(self, pairs=None):
        data = {'pairs': pairs if pairs else []}
        rs_data = self.requests_call_func(method='PUT', url=self.base_url + '/match', data=data)
        return rs_data

    def change_grade_api_call(self, commands=None):
        data = {'commands': commands if commands else []}
        rs_data = self.requests_call_func(method='PUT', url=self.base_url + '/change_grade', data=data)
        return rs_data

    def score_api_call(self):
        rs_data = self.requests_call_func(method='GET', url=self.base_url + '/score')
        return rs_data

    def requests_call_func(self, method, url, headers=None, data=None):
        if not headers:
            headers = {
                'Authorization': self.auth_key,
                'Content-Type': 'application/json'
            }
        if method == 'GET':
            response = requests.get(url=url, headers=headers)
        elif method == 'POST':
            response = requests.post(url=url, data=json.dumps(data), headers=headers)
        elif method == 'PUT':
            response = requests.put(url=url, data=json.dumps(data), headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url=url, data=json.dumps(data), headers=headers)
        else:
            return {}

        if response.status_code == 200:
            rs_data = json.loads(response.text)
            return rs_data
        else:
            print(str(response.text))


class PlayerInfo(object):

    def __init__(self):
        self.player_mmr = {i: 1000 for i in range(1, 31 if PROBLEM == 1 else 901)}  # {id: mmr}

    def get_all_player(self):
        return self.player_mmr

    def get_player_mmr(self, player_id):
        return self.player_mmr[player_id]

    def set_player_mmr(self, player_id, mmr):
        self.player_mmr[player_id] = mmr

    def win_rate(self, player1, player2):
        # 유저 A가 이길 확률 = (유저 A의 고유 실력) / (유저 A의 고유 실력 + 유저 B의 고유 실력)
        return (self.player_mmr[player1]) / (self.player_mmr[player1] + self.player_mmr[player2])

    def calc_player_mmr(self, game_result):
        k = 50 - game_result.get('taken')   # 게임시간에 따른 가중치
        rate = self.win_rate(game_result.get('win'), game_result.get('lose'))
        self.player_mmr[game_result.get('win')] += k * (1 - rate)
        self.player_mmr[game_result.get('lose')] += k * (rate - 1)