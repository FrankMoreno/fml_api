from flask import Flask, session, jsonify
from flask_cors import CORS
import fml
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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
    # PARAMETERS: Username + password
    # Call login method on fml
    # RETURN: session/cookies
    
@app.route('/movies', methods=['GET'])
def returnMovies():
    # TODO add check for cookies
    movies = fml.getMovies()
    return jsonify(movies)

@app.route('/leagues', methods=['GET'])
def returnLeagues():
    # TODO add check for cookies
    leagues = fml.getLeagues(session['cookies'])
    return jsonify(leagues)                         

if __name__ == '__main__':        
    app.run(debug=True)
