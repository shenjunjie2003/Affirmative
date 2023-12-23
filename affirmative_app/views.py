"""
views.py
This file is the implementation of the routes for the application.
"""

from flask import render_template, request, redirect, url_for, flash, session
from affirmative_app import app
#from affirmative_app import db

def login():
    return render_template('login.html')