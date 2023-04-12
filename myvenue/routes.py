from flask import render_template
from myvenue import app, db


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/listings")
def listings():
    return render_template("listings.html")
