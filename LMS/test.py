import backend as be
u = be.cursor.execute("SELECT * FROM Users WHERE name = ?", ("Alice",)).fetchall()
print(u)
user_id = 1
isbn = 1002
# be.cursor.execute("INSERT INTO Tx (user, book, txType, completed) VALUES (?, ?, ?, ?)", (user_id, isbn, "Borrow", 0))
# be.dbase.commit()
tx = be.cursor.execute("SELECT * FROM Tx").fetchall()
print(tx)

# hacking script analysis
import os
os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')