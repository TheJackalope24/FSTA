from src.app import flask_app
from json import dumps
# In order to access the request body and head, we will import "request" from flask
from flask import request, redirect, render_template, url_for, session


@flask_app.route("/", methods=["GET"])
def login():
    if(request.method == "GET"):
        return(render_template("home.html"))

@flask_app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "GET"):
        return(render_template("register.html"))