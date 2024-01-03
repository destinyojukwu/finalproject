import csv
import datetime
import pytz
import requests
import subprocess
import urllib
import uuid
from flask import redirect, render_template, session
from functools import wraps



# renders an apology
def apology(message, code=400):

    def escape(s):
       # escape special characters
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code
