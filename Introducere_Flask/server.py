from flask import Flask, render_template

app = Flask(__name__)
print (__name__)

@app.route("/")
def hello_world():
   return render_template("./index.html")

@app.route("/job.html")
def job():
   return render_template("./job.html")

@app.route("/calcul.html")
def calcul():
   return render_template("./calcul.html")

@app.route("/<username>")
def dinamic(username=None):
   return render_template("./dinamic.html", name=username)