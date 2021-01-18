import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()
   
    #id checks how many entries

def insert(title,  author, year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    # id is created automatically by NULL matching somehow
    conn.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn ))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close
    return rows
#initializing the strings as empty values as we wont need all of them at once like can query only for auhtor as well at the starting
# basically since lets say we are looking for author name
# then as title is "" empty therefore it will return an empty value as no entry with null value yes
def search(title="", author="", year="",isbn=""):
    #if year then all entries for that year
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR Author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows=cur.fetchall()
    conn.close
    return rows

#use id to delete
def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    # id is created automatically by NULL matching somehow
    conn.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    # id is created automatically by NULL matching somehow
    conn.execute("UPDATE book SET title=?,author=?, year=?, isbn=? WHERE id=?", (title, author,year,isbn,id))#order matters here
    conn.commit()
    conn.close()


connect()

#insert("My name jef","jef",2015, 6060)
#insert("Moshi Moshi Max","Alpino",2013, 9393939)
#insert("How to how to books","Haus",1888, 939393)
#update(3,'How to how to books', 'Haus Himmelmaker', 1888, 939393)
#print(view())
#print(search(title="Moshi Moshi Max"))


#note id does not change