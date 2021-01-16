from flask import Flask
#FLask class object from flas

#initializing the class 
app=Flask(__name__)


@app.route("/")
def home():
    return "Hellloooooooooo"

@app.route("/about/")
def about():
    return "giii"


if __name__=="__main__":
    app.run(debug=True)