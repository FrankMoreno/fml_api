import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'https://sso.noovie.com/login?appKey=fml_web/login-confirm'
MOVIES_URL = 'https://fantasymovieleague.com/checkoutmovies'
payload = {
    'emailAddress': 'Frank.Moreno95@gmail.com',
    'password': ''
}
Movies = {}

with requests.Session() as session:
    session.post(LOGIN_URL, data=payload)
    r = session.get(MOVIES_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    for movieRow in soup.find("tbody").contents:
        bux = movieRow.find("td",class_='movie-price numeric stat sorted first').get_text()
        name = movieRow.find("td",class_='movie-info').div.div.h3.get_text()
        Movies[name] = bux

print(Movies)

# After this line is work in progress
def login(email, password):
    LOGIN_URL = 'https://sso.noovie.com/login?appKey=fml_web/login-confirm'
    payload = {
        'emailAddress': email,
        'password': password
    }
    
    session = requests.Session()
    session.post(LOGIN_URL, data=payload)
    
    return session

def getMovies(session):
    MOVIES_URL = 'https://fantasymovieleague.com/checkoutmovies'
    Movies = {}
    
    response = session.get(MOVIES_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    for movieRow in soup.find("tbody").contents:
        bux = movieRow.find("td",class_='movie-price numeric stat sorted first').get_text()
        name = movieRow.find("td",class_='movie-info').div.div.h3.get_text()
        Movies[name] = bux
        
    return Movies

def getLeagues(session):
    LEAGUES_URL = 'https://fantasymovieleague.com/league/directory'
    Leagues = {}
