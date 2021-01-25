#install flask 
#point to activate to trigger virtual python

from flask import Flask, render_template, request

#note ext has been deprectiated
from flask_sqlalchemy import SQLAlchemy

#__name__ is the name of the current Python module
app=Flask(__name__)

#making connection to the database
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:postgres1234@localhost:5432/height_collector"

db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    
    #datatype of column, primary key??
    id=db.Column(db.Integer, primary_key=True)
    
    #length of string 120, only unique emails
    email_=db.Column(db.String(120), unique=True)

    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_


#creating db
#command line
# . virtual/bin/activate
# from app import db
# 



###############################################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        height=request.form["height_name"]
        print(email)
    return render_template("success.html")

#if script is being executed and not imported  i.e is 
# the main script
if __name__== "__main__":
    app.debug=True
    app.run()
