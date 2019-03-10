from flask import Flask, jsonify, request
from flask_cors import CORS
import fml
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_KEY')
CORS(app)

@app.route('/', methods=['GET'])
def heartBeat():
    return '{"Status": "Server is up."}'

@app.route('/login', methods=['POST'])
def login():
    token = fml.login(request.args.get('email'),request.args.get('password'))
    return jsonify({"authToken" : token})

@app.route('/movies', methods=['GET'])
def returnMovies():
    movies = fml.getMovies()
    return jsonify(movies)

@app.route('/leagues', methods=['GET'])
def returnLeagues():
    authToken = request.args.get('authToken')
    leagues = fml.getLeagues({'ku':authToken})
    return jsonify(leagues)                        

@app.route('/estimates', methods=['GET'])
def returnEstimates():
    estimates = fml.getEstimates()
    return jsonify(estimates)

if __name__ == '__main__':        
    app.run(debug=True)
