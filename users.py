from flask import Flask
from flask import Flask, request, jsonify, g
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = make_dicts
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.cli.command('init')
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/userlist', methods=['GET'])
def users_all():
    all_users = query_db('SELECT * FROM users;')
    return jsonify(all_users)

@app.route('/followerlist', methods=['GET'])
def followers_all():
    all_followers = query_db('SELECT * FROM followers;')
    return jsonify(all_followers)

@app.route('/users', methods=['POST'])
def createUser():
    try:
        query_params = request.get_json()
        username = query_params['username']
        password = query_params['password']
        email = query_params['email']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        db = get_db()
        query_db('INSERT INTO users(username,password,email) VALUES (?,?,?);',(username,hashed_password,email))
        db.commit()
        response = jsonify({"status": "Created" })
        response.status_code = 201
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    except Exception:
        response = jsonify({"status": "Bad Request" })
        response.status_code = 400
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

@app.route('/authenticate', methods=['POST'])
def authenticateUser():
    try:
        query_params = request.get_json()
        requested_user = query_params['username']
        requested_pass = query_params['password']
 
        username = query_db('SELECT password FROM users WHERE username = ?;',(requested_user,))
        hashed_pass = username[0]['password']
        print(hashed_pass)
        result = check_password_hash(hashed_pass,requested_pass)
        if result == True:
            response = jsonify({"status": "Authorized" })
            response.status_code = 200
            response.headers["Content-Type"] = "application/json; charset=utf-8"
            return response

        else:
            message = {'message': "Unauthorized"}
            resp = jsonify(message)
            resp.status_code = 401
            resp.headers["Content-Type"] = "application/json; charset=utf-8"
            return resp
    except Exception:
        response = jsonify({"status": "Bad Request" })
        response.status_code = 400
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

@app.route('/follow', methods=['POST'])
def addFollower():
    try:
        query_params = request.get_json()
        username = query_params['username']
        follower = query_params['follower']

        db = get_db()
        query_db('INSERT INTO followers(username,follower) VALUES (?,?);',(username,follower))
        db.commit()
        response = jsonify({"status": "OK" })
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    except Exception:
        response = jsonify({"status": "Bad Request" })
        response.status_code = 400
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

@app.route('/unfollow', methods=['DELETE'])
def removeFollower():
    try:
        query_params = request.get_json()
        username = query_params['username']
        follower = query_params['follower']

        db = get_db()
        query_db('DELETE FROM followers WHERE username = ? AND follower = ?',(username,follower))
        db.commit()
        response = jsonify({"status": "OK" })
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    except Exception:
        response = jsonify({"status": "Bad Request" })
        response.status_code = 400
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response