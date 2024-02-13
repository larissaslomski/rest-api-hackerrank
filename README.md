### Rest API (Intermediate) Skills Certification Test
## Desafio 01: Total goals by a team
O objetivo deste desafio era utilizar de requests em python e lidar com os reponses utilizando paginação e manipulação de json para pegar informações do numero total de gols de um determinado time e ano.

```
Input: team, year
GET request: https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1=<team>&page=<page>
Response:
{
    "page": 1,
    "per_page": 10,
    "total": 6,
    "total_pages": 1,
    "data": [
        {
            "competition": "UEFA Champions League",
            "year": 2011,
            "round": "GroupH",
            "team1": "Barcelona",
            "team2": "AC Milan",
            "team1goals": "2",
            "team2goals": "2"
        },... }
}
Output: um inteiro do numero total de gols.
```

## Desafio 02: Number of drawn matches

Semelhante ao objetivo do desafio 01, este se diferencia ao determinar um timeout caso a response demore ao percorrer as páginas para pegar o numero de drawns (quando um time e seu adversário fazem o mesmo número de gols em uma partida) de um determinado ano. Permitindo exercitar melhoria de desempenho do código e da request.

```
Input: year
GET request: https://jsonmock.hackerrank.com/api/football_matches?year={year}&page=<page>
Response:
{
    "page": 1,
    "per_page": 10,
    "total": 6,
    "total_pages": 1,
    "data": [
        {
            "competition": "UEFA Champions League",
            "year": 2011,
            "round": "GroupH",
            "team1": "Barcelona",
            "team2": "AC Milan",
            "team1goals": "2",
            "team2goals": "2"
        },... }
}
Output: um inteiro do número total de drawns.
```


