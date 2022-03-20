import sqlite3

con = sqlite3.connect('experement.db')

cur = con.cursor()

first_name = str(input())
second_name = str(input())
id_number = int(input())

def createElement():
    cur.execute("INSERT INTO passport VALUES ('{}','{}',{})".format(first_name, second_name, id_number))

createElement()

con.commit()

con.close()