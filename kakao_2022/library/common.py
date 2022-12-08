import json
import requests

from config.settings import *


class GameMatchingRequester(object):

    def __init__(self, problem):
        self.auth_key = None
        self.problem = problem
        self.start_app_call()

    def start_app_call(self):
        headers = {
            'X-Auth-Token': X_AUTH_TOKEN,
            'Content-Type': 'application/json'
        }
        data = {'problem': self.problem}
        rs_data = self.requests_call_func(method='POST', url=BASE_URL + '/start', headers=headers, data=data)
        self.auth_key = rs_data.get('auth_key')

    def waiting_api_call(self):
        rs_data = self.requests_call_func(method='GET', url=BASE_URL + '/waiting_line')
        return rs_data.get('waiting_line')

    def game_result_api_call(self):
        rs_data = self.requests_call_func(method='GET', url=BASE_URL + '/game_result')
        return rs_data.get('game_result')

    def user_info_api_call(self):
        rs_data = self.requests_call_func(method='GET', url=BASE_URL + '/user_info')
        return rs_data.get('user_info')

    def match_api_call(self, pairs=None):
        data = {'pairs': pairs if pairs else []}
        rs_data = self.requests_call_func(method='PUT', url=BASE_URL + '/match', data=data)
        return rs_data

    def change_grade_api_call(self, commands=None):
        data = {'commands': commands if commands else []}
        rs_data = self.requests_call_func(method='PUT', url=BASE_URL + '/change_grade', data=data)
        return rs_data

    def score_api_call(self):
        rs_data = self.requests_call_func(method='GET', url=BASE_URL + '/score')
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
