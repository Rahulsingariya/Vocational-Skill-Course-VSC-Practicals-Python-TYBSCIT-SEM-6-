from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "tyit flask home page"

@app.route("/tyit1")
def tyit1():
    return "tyit flask class 1 task"

@app.route("/tyit2")
def tyit2():
    return "tyit flask class 2 task"

@app.route("/<uname>")
def tyit3(uname):
    return "tyit flask task " + uname

if __name__ == "__main__":
    app.run(debug=True)
