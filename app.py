from flask import Flask, request, render_template
import joblib

dbsModel = joblib.load('DBS_SGD.pkl')
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    q=request.form.get("q")
    return(render_template("main.html"))

@app.route("/dbs", methods=["GET", "POST"])
def dbs():
    return render_template("dbs.html")

@app.route("/dbsPred", methods=["GET", "POST"])
def dbsPred():
    q = float(request.form.get("q"))
    r = dbsModel.predict([[q]])
    return render_template("dbsPred.html", r=r[0][0])

if __name__ == "__main__":
    app.run()