import flask
import requests
from bs4 import BeautifulSoup

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def heartBeat():
    #return getMovies()
    return 'Server is up.'

def getMovies():
    POST_LOGIN_URL = 'https://sso.noovie.com/login?appKey=fml_web/login-confirm'

    #This URL is the page you actually want to pull down with requests.
    REQUEST_URL = 'https://fantasymovieleague.com/checkoutmovies'

    payload = {
        'emailAddress': 'Frank.Moreno95@gmail.com',
        'password':'
    }

    with requests.Session() as session:
        post = session.post(POST_LOGIN_URL, data=payload)
        r = session.get(REQUEST_URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        #return soup.prettify()
        print(soup.find_all("div", class_="movie-info"))
        
app.run()
