from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename
from latlon import latlon_func


app=Flask(__name__)

###############################################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=="POST":
        
        global file
        file=request.files["file"]        
        #saving file

        file.save(secure_filename("uploaded"+ file.filename))
        #with open("uploaded"+file.filename, 'a+') as f:
            #f.write("This was added later aaa")
        latlon_func()
        
        #print("3333334565456787654567876545678765456789")
        #print(file.filename[-3:])
        if file.filename[-3:] != "csv" :
            return render_template("index.html", error1="error1.html")
        else:   
            return render_template("index.html", btn="download.html",table="edited.html")


@app.route('/download')
def download():

    
    return send_file("edited.csv",attachment_filename="yourfile.csv", as_attachment=True)



#explains flask pretty well https://www.youtube.com/watch?v=sy1MNWt7om4

if __name__== "__main__":
    app.debug=True
    app.run()
