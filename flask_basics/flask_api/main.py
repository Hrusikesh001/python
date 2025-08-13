from flask import Flask, jsonify

app = Flask(__name__)



@app.route("/")
def json():
    marks = {
         "John": 90,
         "Alice": 85,
         "Bob": 95,
         "Charlie": 80,
         "David": 92,
         "Eve": 88
    }
    values = [1, marks, 67]
    return jsonify(values)

app.run(debug=True)