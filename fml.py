import requests
from bs4 import BeautifulSoup

# All these methods should return actual response objects

def login(email, password):
    LOGIN_URL = 'https://fantasymovieleague.com/auth/loginconfirm'
    payload = {
        'emailAddress': email,
        'password': password
    }
    
    session = requests.Session()
    session.post(LOGIN_URL, data=payload)
    if 'ku' in session.cookies.get_dict():
        return (session.cookies.get_dict())['ku']
    else:
        return '{}'

def getMovies():
    MOVIES_URL = 'https://fantasymovieleague.com/checkoutmovies'
    Movies = {"movies":[]}

    session=requests.Session()
    response = session.get(MOVIES_URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    for movieRow in soup.find("tbody").contents:
        temp = {
            "bux": movieRow.select_one('td[class*="movie-price numeric"]').get_text(),
            "name": movieRow.find("div",class_='movie-info-name').h3.get_text(),
            "posterLink": movieRow.find("div",class_='movie-info').a['data-img-src']
        }
        Movies["movies"].append(temp)  

    return Movies

def getLeagues(newCookies):
    LEAGUES_URL = 'https://fantasymovieleague.com/league/directory'
    Leagues = {}

    try:
        session=requests.Session()
        response = session.get(LEAGUES_URL, cookies=newCookies)

        soup = BeautifulSoup(response.text, 'html.parser')
        leagueRows = soup.find("table",class_='tableType-league noLeagues').tbody
        for leagueRow in leagueRows.find_all("tr"):
            leagueName = leagueRow.find("td",class_='league-name first').a.get_text()
            leagueLink = leagueRow.find("td",class_='league-name first').a['href']
            Leagues[leagueName] = {'link':leagueLink}
    except:
        Leagues = {"Error":"Unknown exception"}

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
    # print(getLeagues())
    print(getMovies())
    # print(getEstimates())

if __name__ == '__main__':
    main()
