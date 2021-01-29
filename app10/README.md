#Setting up heroku

you need to set up a git repository. 3 files requirements.txt, proc, runtime.txt. 

Also a small change in app.py file. Change local database postgres to Heroku Database. 

So need to create a heroku.

heroku login.

Database is an add on.

USE CLI to make database.
 
 >heroku create avidbase

 >  heroku-postgresql:hobby-dev --app avidbase--app avidbase
 10,000 records cap

 Method to get the URI 

 > heroku config --app avidbase


postgres://xvelxqcbmxgxjd:9dd39d36b58835f3939857f58f40765d3a39c747889d7598cf2fe7f207418331@ec2-3-214-4-151.compute-1.amazonaws.com:5432/d2kfnk64rtkhr8

## Making the req files

virtual environment first

install gunicornss
pip freeze > requirements.txt


heroku git:remote --app avidbase
git push heroku master


another point to remember is that make seperate git for this does not work when in udemy folder