from flask import Flask, session, jsonify
import requests
import fml

app = Flask(__name__)

@app.route('/', methods=['GET'])
def heartBeat():
    return 'Server is up.'

@app.route('/login', methods=['POST'])
def login():
    fml.login('Frank.Moreno95@gmail.com','*******')
    print('You logged in.')
    # PARAMETERS: Username + password
    # Call login method on fml
    # RETURN: session/cookies
    
@app.route('/movies', methods=['GET'])
def returnMovies():
    movies = fml.getMovies(session)
    return jsonify(movies)
    # PARAMETERS: Username + password                         
    # Call get movies with session
    # RETURN: list of movies in JSON                          
        
app.run()
