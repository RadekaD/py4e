import sqlite3

conn =  sqlite3.connect("py4e_emaildb.sqlite")
cur =  conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)' )

fname = input("Enter file name: ")
#with 
fhand = open(fname)


for line in fhand:
    if not line.startswith("From: "): continue
    words = line.split()
    email = words[1]
    host = email.split("@")[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (host,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (host,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (host,))
    
conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
