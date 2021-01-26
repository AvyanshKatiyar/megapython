#install flask 
#point to activate to trigger virtual python

from flask import Flask, render_template, request

#note ext has been deprectiated
from flask_sqlalchemy import SQLAlchemy
#__name__ is the name of the current Python module
from send_email import send_email

#average 
from sqlalchemy.sql import func


app=Flask(__name__)

#making connection to the database
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:postgres1234@localhost:5433/height_collector"
#local host was missing

#heroku dbase
#?sslmode=require
#app.config["SQLALCHEMY_DATABASE_URI"]="postgres://xvelxqcbmxgxjd:9dd39d36b58835f3939857f58f40765d3a39c747889d7598cf2fe7f207418331@ec2-3-214-4-151.compute-1.amazonaws.com:5432/d2kfnk64rtkhr8?sslmode=require"
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
#db.create_all()



###############################################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=="POST":
        
        email=request.form["email_name"]
        height=request.form["height_name"]
        #print(email, height)
        

        # delete from data where email_='email' NOTE that the single quotes are very important
        # select * from data to get query as object is data
        #adding to the database
            
            # gives number of email already in email 
        if db.session.query(Data).filter(Data.email_==email).count() ==0:   
            data=Data(email, height)
            db.session.add(data)
            db.session.commit()
            


            #finding the average value
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height, 1)
            print(average_height)
            count=db.session.query(Data.height_).count()
            send_email(email, height,average_height, count )

            return render_template("success.html")
        else:
            return render_template("index.html", text= "Moshi moshi, already have your height")
            #NOTE if change does not show up then clear browser cache
#if script is being executed and not imported  i.e is 
# the main script
if __name__== "__main__":
    app.debug=True
    app.run()
