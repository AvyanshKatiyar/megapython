import mysql.connector

#credentioals psdd below
con = mysql.connector.connect(
user="ardit700_student",
password="ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)

#creates cursor
cursor= con.cursor()
# * means all dictionary table
#query = cursor.execute("SELECT * FROM Dictionary")
word=input("Give your word: ")
# above statement gets all of the elements in the dictionary note the dictioanry is a list of tuples
#gets one tupple
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'"%word)
#fetches all from the quers
results= cursor.fetchall()

#if results is a boolean that checks whether results is an empty list or not
if results:
    for result in results:    
        print(result[1]) #("key", "vslue") printing value
else:
    print("No word found:")


##query = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression)<4" also works ok

