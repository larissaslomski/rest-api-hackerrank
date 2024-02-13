import requests

def getNumDraws(year):
    drawns = 0

    for goal in range(0, 10):
        response = requests.get(
            f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={goal}&team2goals={goal}")
        drawns += int(response.json()['total'])
    return drawns


draws = getNumDraws(2012)
print()