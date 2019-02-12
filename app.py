from flask import Flask, session, jsonify
from flask_cors import CORS
import fml
import json
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_KEY')
CORS(app)

@app.route('/', methods=['GET'])
def heartBeat():
    return '{"Status": "Server is up."}'

@app.route('/login', methods=['GET'])
def login():
    # TODO Add check if user is already logged in
    newCookies = fml.login('Frank.Moreno95@gmail.com','Tacos123')
    session['cookies'] = json.dumps(newCookies)
    return 'You logged in'
    
@app.route('/movies', methods=['GET'])
def returnMovies():
    movies = fml.getMovies()
    return jsonify(movies)

@app.route('/leagues', methods=['GET'])
def returnLeagues():
    # TODO add check for cookies
    leagues = fml.getLeagues(session['cookies'])
    return jsonify(leagues)                         

# TODO Add estimates route
@app.route('/estimates', methods=['GET'])
def returnEstimates():
    estimates = fml.getEstimates()
    return jsonify(estimates)

if __name__ == '__main__':        
    app.run(debug=True)
