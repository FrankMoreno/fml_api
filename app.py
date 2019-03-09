from flask import Flask, session, jsonify, request
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

@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if 'cookies' in session:
        response = jsonify({"Status" : "User already logged in"})
    else:
        newCookies = fml.login(request.args.get('email'),request.args.get('password'))
        session['cookies'] = json.dumps(newCookies)
        # return jsonify({'sessionID':session['cookies']})
        response = jsonify({"Status" : "Login successful"})
    response.headers.add('Access-Control-Allow-Origin', 'true')
    return response

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('cookies', None)
    return jsonify({"Status" : "Logout successful"})

@app.route('/movies', methods=['GET'])
def returnMovies():
    movies = fml.getMovies()
    return jsonify(movies)

@app.route('/leagues', methods=['GET'])
def returnLeagues():
    if 'cookies' in session:
        leagues = fml.getLeagues(session['cookies'])
        return jsonify(leagues)
    else:
        return jsonify({})                         

@app.route('/estimates', methods=['GET'])
def returnEstimates():
    estimates = fml.getEstimates()
    return jsonify(estimates)

if __name__ == '__main__':        
    app.run(debug=True)
