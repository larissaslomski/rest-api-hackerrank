import requests

def getTotalGoals(team, year):
    total_goals = 0
    total_pages_team_1 = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page=1").json()['total_pages']
    total_pages_team_2 = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page=1").json()['total_pages']

    for page_team_1 in range(1, total_pages_team_1 + 1):
        data_team_1_by_page = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page_team_1}").json()['data']
        for competition_team_1 in data_team_1_by_page:
            total_goals += int(competition_team_1['team1goals'])

    for page_team_2 in range(1, total_pages_team_2 + 1):
        repsonse_team_2 = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page_team_2}").json()
        data_team_2_by_page = repsonse_team_2['data']
        for competition_team_2 in data_team_2_by_page:
            total_goals += int(competition_team_2['team2goals'])

    return total_goals