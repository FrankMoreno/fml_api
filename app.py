import flask
import requests
from bs4 import BeautifulSoup

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def heartBeat():
    return 'Server is up.'

@app.route('/login', methods['POST'])
def login():
    # PARAMETERS: Username + password
    # Call login method on fml
    # RETURN: session/cookies
    
@app.route('/movies', methods['GET])
def returnMovies():
    # PARAMETERS: Username + password                         
    # Call get movies with session
    # RETURN: list of movies in JSON                          
        
app.run()
