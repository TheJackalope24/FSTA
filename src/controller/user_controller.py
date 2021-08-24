from src.app import flask_app
from json import dumps
# In order to access the request body and head, we will import "request" from flask
from flask import request, redirect, render_template, url_for, session
from src.service import user_service


@flask_app.route("/", methods=["GET", "POST"])
def login():
    if(request.method == "GET"):
        return(render_template("home.html"))
    elif(request.method == "POST"):
        return(user_service.login(request.get_json()))

@flask_app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "GET"):
        return(render_template("register.html"))
    elif(request.method == "POST"):
        return(user_service.register(request.get_json()))
        
@flask_app.route("/dashboard/<username>", methods=["GET"])
def dashboard(username):
    if(request.method == "GET"):
        return(render_template("dashboard.html"))