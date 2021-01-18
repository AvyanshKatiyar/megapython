import sqlite3

#connect
#cursor
#sql query
#commit changes
#close connection

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #use single quotes not double to add another row repeat par bt because insert twice
    conn.commit()
    conn.close

def insert(item, quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()



def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    
    cur.execute("DELETE FROM store WHERE item=?",(item,))#remember , after item only when item is one
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))#remember , after item
    conn.commit()
    conn.close()
update(11,22,"Water Glass")

print(view())