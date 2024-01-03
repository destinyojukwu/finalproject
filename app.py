import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology

# MAKE SURE THIS CAN BE VIEWED THE SAME ON DIFFERENT TYPES OF DEVICES
# Configure Flask application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# defines my database
db = SQL("sqlite:///project2.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# process to identify you. you must redo this process everytime you wanna see results
@app.route("/")
def home():
    return render_template("nameinput.html")

@app.route(
    "/nameinput", methods=["GET", "POST"])
def nameinput():
    # registers user in database
    if request.method == "POST":
        username = request.form.get("username")
        if not request.form.get("username"):
            return apology("must provide username", 400)
        # ensures username exists
        rows = db.execute(
                "SELECT * FROM users WHERE username = ?", request.form.get("username")
            )
        # prevents repeat usernames
        if len(rows) != 0:
            return apology("username already taken, please choose another")
        db.execute("INSERT INTO users (username) VALUES (?)", username)
        return redirect(url_for('hairquiz'))

    else:
        return render_template("nameinput.html")

@app.route("/hairquiz", methods = ["GET", "POST"])
# identify hair concern
def hairquiz():
    if request.method == 'POST':
        hairconcern = request.form.get("hair concern?")
        if hairconcern == "curl definition":
            return redirect(url_for('curldefinition'))
        if hairconcern == "dryness":
           return redirect(url_for('dryness'))
        if hairconcern == "damage repair":
            return redirect(url_for('damagerepair'))
        if not hairconcern:
           return apology("must provide hair concern from the list of choices with correct spelling", 400)
        if hairconcern != "curl definition" and hairconcern != "dryness" and hairconcern != "damage repair" :
            return apology("must provide hair concern from the list of choices with correct spelling!")
    if request.method == 'GET':
        return render_template('hairquiz.html')
#the following lines of code route the user to the page that matches their hair concern
@app.route("/curldefinition", methods = ["GET", "POST"])
def curldefinition():
    return render_template("curldefinition.html")

@app.route("/dryness", methods = ["GET", "POST"])
def dryness():
    return render_template("dryness.html")

@app.route("/damagerepair", methods = ["GET", "POST"])
def damagerepair():
    return render_template("damagerepair.html")