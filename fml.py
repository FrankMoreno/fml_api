import requests
from bs4 import BeautifulSoup
import json

def login(email, password):
    LOGIN_URL = 'https://fantasymovieleague.com/auth/loginconfirm'
    payload = {
        'emailAddress': email,
        'password': password
    }
    
    session = requests.Session()
    session.post(LOGIN_URL, data=payload)

    return session.cookies.get_dict()

def getMovies():
    MOVIES_URL = 'https://fantasymovieleague.com/checkoutmovies'
    Movies = {"movies":[]}

    session=requests.Session()
    response = session.get(MOVIES_URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    for movieRow in soup.find("tbody").contents:
        temp = {}
        temp["bux"] = movieRow.find("td",class_='movie-price numeric stat first').get_text()
        temp["name"] = movieRow.find("td",class_='movie-info').div.div.h3.get_text()
        Movies["movies"].append(temp)  
    return Movies

def getLeagues(newCookies):
    LEAGUES_URL = 'https://fantasymovieleague.com/league/directory'
    Leagues = {}
    newCookies = json.loads(newCookies)

    session=requests.Session()
    response = session.get(LEAGUES_URL, cookies=newCookies)

    soup = BeautifulSoup(response.text, 'html.parser')
    leagueRows = soup.find("table",class_='tableType-league noLeagues').tbody
    for leagueRow in leagueRows.find_all("tr"):
        leagueName = leagueRow.find("td",class_='league-name first').a.get_text()
        leagueLink = leagueRow.find("td",class_='league-name first').a['href']
        Leagues[leagueName] = {'link':leagueLink}

    return Leagues

def submitPicks():
    Picks = {}
    return Picks
    
def getPicks():
    Picks = {}
    return Picks

def main():
    cookies = login("Frank.Moreno95@gmail.com", "Tacos123")
    print(getLeagues(cookies))
    print(getMovies())

if __name__ == '__main__':
    main()
