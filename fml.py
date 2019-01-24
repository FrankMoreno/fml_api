import requests
from bs4 import BeautifulSoup

def login(email, password):
    LOGIN_URL = 'https://fantasymovieleague.com/auth/loginconfirm'
    payload = {
        'emailAddress': email,
        'password': password
    }
    
    session = requests.Session()
    response = session.post(LOGIN_URL, data=payload)
    return session

def getMovies(session):
    MOVIES_URL = 'https://fantasymovieleague.com/checkoutmovies'
    Movies = {}
    
    response = session.get(MOVIES_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    for movieRow in soup.find("tbody").contents:
        bux = movieRow.find("td",class_='movie-price numeric stat sorted first').get_text()
        name = movieRow.find("td",class_='movie-info').div.div.h3.get_text()
        Movies[name] = bux
        
    return Movies

def getLeagues(session):
    LEAGUES_URL = 'https://fantasymovieleague.com/league/directory'
    Leagues = {}

    response = session.get(LEAGUES_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    leagueRows = soup.find("table",class_='tableType-league noLeagues').tbody
    for leagueRow in leagueRows.find_all("tr"):
        print(leagueRow.find("td",class_='league-name first').a.get_text())
        # TO-DO get href
        # TO-DO get rankings
    
    return Leagues

def submitPicks():
    Picks = {}
    
def getPicks():
    Picks = {}

def main():
    session = login("Frank.Moreno95@gmail.com", "Tacos123")
    getLeagues(session)
    getMovies(session)

if __name__ == '__main__':
    main()
