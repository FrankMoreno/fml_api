from flask import Flask, session, jsonify
import requests
import fml
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def heartBeat():
    return 'Server is up.'

@app.route('/login', methods=['GET'])
def login():
    # TODO Add check if user is already logged in
    newCookies = fml.login('Frank.Moreno95@gmail.com','*******')
    session['cookies'] = json.dumps(newCookies)
    return 'You logged in'
    # PARAMETERS: Username + password
    # Call login method on fml
    # RETURN: session/cookies
    
@app.route('/movies', methods=['GET'])
def returnMovies():
    # TODO add check for cookies
    movies = fml.getMovies(session['cookies'])
    return jsonify(movies)

@app.route('/leagues', methods=['GET'])
def returnLeagues():
    # TODO add check for cookies
    leagues = fml.getLeagues(session['cookies'])
    return jsonify(leagues)                         
        
#app.run(debug=True)
