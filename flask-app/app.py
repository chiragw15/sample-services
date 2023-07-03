import os
from flask import Flask, jsonify
from flaskext.mysql import MySQL
from flask_redis import FlaskRedis

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_DATABASE_HOST')
mysql = MySQL(app)

# Redis Configuration
app.config['REDIS_URL'] = os.environ.get('REDIS_URL')
redis_store = FlaskRedis(app)

@app.route('/ping', methods=['GET'])
def ping():
    try:
        # Check MySQL connection
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        if not result:
            return jsonify({'mysql': 'unavailable'}), 500

        # Check Redis connection
        pong = redis_store.ping()
        if not pong:
            return jsonify({'redis': 'unavailable'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
