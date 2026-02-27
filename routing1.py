from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/tyit1")
def tyit1():
    return "tyit flask class 1 task"

@app.route("/<uname>")
def tyit2(uname):
    return "tyit flask task " + uname

if __name__ == "__main__":
    app.run(debug=True)
