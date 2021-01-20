import sqlite3
#initializing the class

#database is the onject
class Database:  
    #init  initializes the object dont need to call
    #init is a type of constructor it executes even without reffering to it 
   #since we are calling Database() it is returning an argument null so we pass an argument self by default else error
    def __init__(self):
        #adding attributes to object self self.conn is attribute of self
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

        #id checks how many entries

    def insert(self, title,  author, year,isbn):
        # id is created automatically by NULL matching somehow
        self.conn.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn ))
        self.conn.commit()
    #object is sent to method again
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows
    #initializing the strings as empty values as we wont need all of them at once like can query only for auhtor as well at the starting
    # basically since lets say we are looking for author name
    # then as title is "" empty therefore it will return an empty value as no entry with null value yes
    def search(self, title="", author="", year="",isbn=""):
        #if year then all entries for that year
        self.cur.execute("SELECT * FROM book WHERE title=? OR Author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    #use id to delete
    def delete(self, id):
       
        # id is created automatically by NULL matching somehow
        self.conn.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id,title, author, year, isbn):
   
        # id is created automatically by NULL matching somehow
        self.conn.execute("UPDATE book SET title=?,author=?, year=?, isbn=? WHERE id=?", (title, author,year,isbn,id))#order matters here
        self.conn.commit()
    
    #run when script exucutes 
    def __del__(self):
        self.conn.close()


#insert("My name jef","jef",2015, 6060)
#insert("Moshi Moshi Max","Alpino",2013, 9393939)
#insert("How to how to books","Haus",1888, 939393)
#update(3,'How to how to books', 'Haus Himmelmaker', 1888, 939393)
#print(view())
#print(search(title="Moshi Moshi Max"))


#note id does not change