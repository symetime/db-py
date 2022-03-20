import sqlite3

con = sqlite3.connect('experement.db')

cur = con.cursor()

cur.execute('''CREATE TABLE passport
               (first_name text, last_name text, id Int)''')

con.commit()

con.close()