import requests
from bs4 import BeautifulSoup
import time
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
    # TODO Add link to movie poster picture
    for movieRow in soup.find("tbody").contents:
        temp = {}
        temp["bux"] = movieRow.find("td",class_='movie-price numeric stat first').get_text()
        temp["name"] = movieRow.find("div",class_='movie-info-name').h3.get_text()
        temp["posterLink"] = movieRow.find("div",class_='movie-info').a['data-img-src']
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

def getEstimates():
    # TODO Need to pull data from multiple sources and average them
    # TODO will eventually need to check if one estimate is outdated
    ESTIMATES_URL = 'http://www.boxofficereport.com/predictions/predictions.html'
    Estimates = {"estimates":[]}
    
    session=requests.Session()
    response = session.get(ESTIMATES_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    moviesTable = (soup.find_all("table"))[2] # There are multiple tables on the page and none have unique identifiers
    movieRows = moviesTable.find_all('tr')[1:]
    for movieRow in movieRows:
        cells = movieRow.find_all('td')
        temp = {}
        # TODO Clean up this monstrosity, probably just use a regex
        temp['name'] = ((cells[1].get_text()).split('(')[0]).strip()
        temp['estimate'] = cells[2].get_text()
        Estimates['estimates'].append(temp)
        
    return Estimates

def submitPicks():
    Picks = {}
    return Picks
    
def getPicks():
    Picks = {}
    return Picks

def main():
    cookies = login("Frank.Moreno95@gmail.com", "Tacos123")
    # print(getLeagues(cookies))
    print(getMovies())
    getEstimates()

if __name__ == '__main__':
    main()
