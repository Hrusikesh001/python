from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John": 90,
        "Alice": 85,
        "Bob": 95,
        "Charlie": 80,
        "David": 92,
        "Hrusi": 1
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)