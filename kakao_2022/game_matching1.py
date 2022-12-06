import json
import requests

class GameMatchingRequester(object):

    def __init__(self, problem):
        self.base_url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
        self.x_auth_token = 'ebbb2ffefb936541d51c5a0df1362ed7'
        self.problem = problem
        self.auth_key = self.start_app_call()  # auth_key setting

    def start_app_call(self):
        url = self.base_url + '/start'
        data = {'problem': self.problem}
        headers = {
            'X-Auth-Token': self.x_auth_token,
            'Content-Type': 'application/json'
        }
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            result = json.loads(response.text)
            auth_key = result.get('auth_key')
            if auth_key:
                return auth_key
        else:
            return None

    def waiting_api_call(self):
        rs_data = self.requests_call_func(method='GET', url='/waiting_line')
        return rs_data.get('waiting_line')

    def game_result_api_call(self):
        rs_data = self.requests_call_func(method='GET', url='/game_result')
        return rs_data.get('game_result')

    def user_info_api_call(self):
        rs_data = self.requests_call_func(method='GET', url='/user_info')
        return rs_data.get('user_info')

    def match_api_call(self, pairs=None):
        data = {'pairs': pairs if pairs else []}
        rs_data = self.requests_call_func(method='PUT', url='/match', data=data)
        return rs_data

    def change_grade_api_call(self, commands=None):
        data = {'commands': commands if commands else []}
        rs_data = self.requests_call_func(method='PUT', url='/change_grade', data=data)
        return rs_data

    def score_api_call(self):
        rs_data = self.requests_call_func(method='GET', url='/score')
        return rs_data

    def requests_call_func(self, method, url, data=None):
        headers = {
            'Authorization': self.auth_key,
            'Content-Type': 'application/json'
        }
        if method == 'GET':
            response = requests.get(url=self.base_url + url, headers=headers)
        elif method == 'POST':
            response = requests.post(url=self.base_url + url, data=json.dumps(data), headers=headers)
        elif method == 'PUT':
            response = requests.put(url=self.base_url + url, data=json.dumps(data), headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url=self.base_url + url, data=json.dumps(data), headers=headers)
        else:
            return {}

        if response.status_code == 200:
            rs_data = json.loads(response.text)
            return rs_data
        else:
            print(str(response.text))


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