from flask import Blueprint, Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from Logic.api import *
from Logic.core import *
import json
from Logic.MySql import * 

app = Flask(__name__)
app.secret_key = "SECRETKEY"

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

@app.route("/")
def Index():
    return redirect(url_for('Login'))

@app.route("/Login", methods=['GET', 'POST'])
def Login():
    if 'loggedin' in session:
        return redirect(url_for('Dashboard'))

    if request.method == "POST" and 'password' in request.form:
        password = request.form['password']
        with open('login.txt') as f:
            data = f.read()
        logins = json.loads(data)
        for login in logins:
            if password == login:
                session['loggedin'] = True
                session['id'] = "DESKTOPID"
                session['name'] = logins[login]
                print(session['name'])
                return redirect(url_for('Dashboard'))
        
        msg = "Incorrect Password"
        
    return render_template('Login.html', msg='')

@app.route("/Dashboard")
def Dashboard():
    if 'loggedin' in session:
        return render_template("Dashboard.html")
    else:
        return redirect(url_for('Login'))

@app.route("/Logout")
def Logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    return redirect(url_for('Login'))

@app.route("/SendImage", methods=['POST'])
def sendImage():
    if 'loggedin' in session and request.method == "POST" and 'img' in request.form:
        if request.method == "POST" and 'img' in request.form:
            status = printImage(request.form['img'])
            return status
    return "Error"

@app.route("/SendMessage", methods=['POST'])
def sendMessage():
    if 'loggedin' in session and request.method == "POST" and 'msg' in request.form:
        status = printMessage(request.form['msg'], session['name'])
        return status
    return "Error"
        


###   API
@app.route("/API/v1/<string:key>/<string:methodName>")
def api(key, methodName):
    if 'loggedin' in session:
        #pre-approved
        return ApiCallStructure(methodName)
    
    if key == "SECRET":
        return ApiCallStructure(methodName)

    else:
        return "API KEY WRONG: ABORTED"
