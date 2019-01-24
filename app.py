import flask
import requests

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def heartBeat():
    return 'Server is up.'

@app.route('/login', methods=['POST'])
def login():
    return "You logged in"
    # PARAMETERS: Username + password
    # Call login method on fml
    # RETURN: session/cookies
    
@app.route('/movies', methods=['GET'])
def returnMovies():
    return "these are your movies"
    # PARAMETERS: Username + password                         
    # Call get movies with session
    # RETURN: list of movies in JSON                          
        
app.run()
