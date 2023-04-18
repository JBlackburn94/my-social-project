from flask import render_template
from myvenue import app, db


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/my_events")
def my_events():
    return render_template("my_events.html")


@app.route("/add_event")
def add_event():
    return render_template("add_event.html")
