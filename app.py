from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/data')
def get_data():
    data = {
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "air_quality": round(random.uniform(200, 500), 2),
        "noise": round(random.uniform(30, 90), 2)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
