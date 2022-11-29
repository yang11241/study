from django.shortcuts import render
import requests
import json
from datetime import datetime


# Create your views here.

def get_qatar_2022_game_list(request):
    result = []
    # 사용자가 api호출한거처럼 하기 위한 headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url = 'https://api-gw.sports.naver.com/schedule/qatar2022/games?fromDate=2022-01-01&toDate=2022-12-31'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        rs_data = json.loads(response.text)
        if 'result' in rs_data:
            if 'games' in rs_data['result']:
                for game in rs_data['result']['games']:
                    result.append({
                        'game_date_time': datetime.strptime(game['gameDateTime'], '%Y-%m-%dT%H:%M:%S').strftime('%Y년 %m월 %d일 %H:%M:%S'),
                        'home_team_name': game['homeTeamName'],
                        'home_team_score': game['homeTeamScore'],
                        'away_team_name': game['awayTeamName'],
                        'away_team_score': game['awayTeamScore'],
                        'winner': game['homeTeamName'] if game['winner'] == 'HOME' else game['awayTeamName'] if game['statusCode'] == 'RESULT' else '',
                        'status_info': game['statusInfo'],
                        'prev_results': game['prevResults'] if game['statusCode'] == 'RESULT' else ''
                    })

    context = {'games': result}
    return render(request, 'qatar2022/index.html', context)
