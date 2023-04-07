from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/module")
def module_for_cs():
    return render_template("module.html")

@app.route("/rank")
def rank():
    return render_template("rank.html")

@app.route("/email")
def email():
    return render_template("email.html")

if __name__ == "__main__":
    app.run(debug=False)
