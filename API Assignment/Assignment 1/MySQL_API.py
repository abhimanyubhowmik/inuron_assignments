import MysqlDB
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/connect',methods = ['GET', 'POST'])
def connect():
    if request.method == 'POST':
        host = request.json['host']
        usr = request.json['user']
        passwd = request.json['pass']

        conn = MysqlDB.Connection(host,usr,passwd)
        return jsonify(str(conn.db()))

    else:
        return jsonify(str('USE POST METHOD FOR SECURED CONNECTION ESTABLISHMENT'))

@app.route('/connect/get_db',methods = ['GET', 'POST'])
def get_db():
    if request.method == 'POST':
        host = request.json['host']
        usr = request.json['user']
        passwd = request.json['pass']

        conn = MysqlDB.Connection(host,usr,passwd)
        cursor = conn.cursor()

        db = MysqlDB.Database(cursor)
        result = db.showDatabase()

        return jsonify(str(result))

    else:
        return jsonify(str('USE POST METHOD FOR SECURED CONNECTION ESTABLISHMENT'))

@app.route('/connect/get_tables',methods = ['GET', 'POST'])
def get_tables():
    if request.method == 'POST':
        host = request.json['host']
        usr = request.json['user']
        passwd = request.json['pass']
        database = request.json['database']

        conn = MysqlDB.Connection(host,usr,passwd)
        cursor = conn.cursor()

        db = MysqlDB.Database(cursor)
        result = db.showTable(database)

        return jsonify(str(result))

    else:
        return jsonify(str('USE POST METHOD FOR SECURED CONNECTION ESTABLISHMENT'))


@app.route('/connect/fetch_data',methods = ['GET', 'POST'])
def fetch_data():
    if request.method == 'POST':
        host = request.json['host']
        usr = request.json['user']
        passwd = request.json['pass']
        database = request.json['database']
        table = request.json['table']

        conn = MysqlDB.Connection(host,usr,passwd)
        cursor = conn.cursor()

        db = MysqlDB.Database(cursor)
        result = db.fetchData(database,table)

        return jsonify(str(result))

    else:
        return jsonify(str('USE POST METHOD FOR SECURED CONNECTION ESTABLISHMENT'))


if __name__ == '__main__':
    app.run(port = 8000)