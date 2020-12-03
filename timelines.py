from flask import Flask, request, jsonify, g, make_response
from flask_caching import Cache
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sqlite3, time

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')

config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app.config.from_mapping(config)
cache = Cache(app)

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

@app.route('/userTimeline', methods = ['GET'])
def getUserTimeline():
    try:
        query_params = request.get_json()
        user = query_params['username']

        tweets = query_db('SELECT text, author, timestamp FROM tweets WHERE author = ? ORDER BY timestamp DESC LIMIT 25;', [user])
        return jsonify(tweets)
    except Exception:
        response = jsonify({"status": "Bad Request" })
        response.status_code = 400
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

@app.route('/publicTimeline',methods=['GET'])
def getPublicTimeline():
    try:
        tweets = query_db('SELECT text, author, timestamp FROM tweets ORDER BY timestamp DESC LIMIT 25;')
        response = make_response(jsonify(tweets))
        get_time = time.time()
        date = str(datetime.fromtimestamp(get_time).strftime('%m-%d-%Y %H:%M:%S'))
        print(date)
        return response.make_conditional(request)
    except Exception:
        response = jsonify({"status": "Bad Request" })
        response.status_code = 400
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

@app.route('/homeTimeline', methods = ['GET'])
def getHomeTimeline():
    try:
        query_params = request.get_json()
        user = query_params['username']

        tweets = query_db('SELECT text, author, timestamp FROM tweets WHERE author IN (SELECT follower FROM followers WHERE username = ?) ORDER BY timestamp DESC LIMIT 25;', [user])
        return jsonify(tweets)
    except Exception:
        response = jsonify({"status": "Bad Request" })
        response.status_code = 400
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

@app.route('/tweets',methods=['POST'])
def postTweet():
    try:
        query_params = request.get_json()
        text = query_params['text']
        timestamp = datetime.utcnow()
        author = query_params['author']

        db = get_db()
        query_db('INSERT INTO tweets(text,timestamp,author) VALUES (?,?,?);',(text,timestamp,author))
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
