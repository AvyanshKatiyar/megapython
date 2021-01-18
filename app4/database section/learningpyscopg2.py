import psycopg2

#connect
#cursor
#sql query
#commit changes
#close connection

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5433' ")
    cur=conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #use single quotes not double to add another row repeat par bt because insert twice
    conn.commit()
    conn.close

def insert(item, quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5433' ")
    cur=conn.cursor()
    
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()



def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5433' ")
    cur=conn.cursor()
    
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5433' ")
    cur=conn.cursor()
    
    cur.execute("DELETE FROM store WHERE item = %s",(item,))#remember , after item only when item is one
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5433' ")
    cur=conn.cursor()
    
    cur.execute("UPDATE store SET quantity=%s, price=%s  WHERE item=%s",(quantity, price, item))#remember , after item
    conn.commit()
    conn.close()
#update(11,22,"Water Glass")

create_table()
#insert("maggi",5,120)
update(30,4000,"pijja")
delete("Samosa")
print(view())
#print(view())