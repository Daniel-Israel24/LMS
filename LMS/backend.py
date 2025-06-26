# this is a command line based library management system
import sqlite3, hashlib
# defining the objects
dbase = sqlite3.connect("G3Lib.db")
cursor = dbase.cursor()

# Fn skeletons
def initdb():
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Books (isbn INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, publisher TEXT NOT NULL, price INTEGER, copies INTEGER)
                   """)
    dbase.commit()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, staff INTEGER, passwd TEXT NOT NULL)
                    """)
    dbase.commit()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Tx (id INTEGER PRIMARY KEY AUTOINCREMENT,user INTEGER, book INTEGER, txType TEXT NOT NULL, completed INTEGER)
                    """)
    dbase.commit()


# book
class Book():
    def __init__(self, title, isbn, author, publisher, price, quantity):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.price = price
        self.quantity = quantity
    def delete(self):
        cursor.execute("DELETE FROM Books WHERE isbn = ?", (self.isbn))
        dbase.commit()
        print(f"Deleted {self.title} by {self.author}")
        
    def changeparam(self, table, param, to_value):
        cursor.execute(f"UPDATE {table} SET {param} = ? WHERE id = {self.id}", (to_value,))
        dbase.commit()
    def add(self):
        cursor.execute("INSERT INTO Books (isbn, title, author, publisher, price, copies) VALUES (?, ?, ?, ?, ?, ?)", (self.isbn, self.title, self.author, self.publisher, self.price, self.quantity))
        dbase.commit()
        
    def lend(self, to_user, n_books):
        self.quantity -= n_books

# user

class User():
    Bought = []
    Borrowed = []
    def __init__(self,id, name,pwd,  staff=0):
        self.name = name
        self.staff_status =staff
        self.id = id
        self.pwdhash = hashlib.sha256(str(pwd).encode()).hexdigest()
    def save(self):
        cursor.execute("INSERT INTO Users (id, name, staff, passwd) VALUES (?, ?, ?, ?)", (self.id, self.name, self.staff_status, self.pwdhash))
        dbase.commit()
        print("Successfully created a user account!")
    def changeparam(self, param, to_value):
        cursor.execute(f"UPDATE Users SET {param} = ? WHERE id = {self.id}", (to_value,))
        dbase.commit()
        
    def borrow(self, book):
        cursor.execute("INSERT INTO Tx (user, book, txType, completed) VALUES (?, ?, ?, ?)", (self.id, book, "Borrow", 0))
        dbase.commit()
        print("Book has been borrowed successfully!")
    def returnbk(self, book):
        cursor.execute(f"DELETE FROM Tx WHERE book = ?", (book,))
        dbase.commit()
        print(f"Successfully deleted the book - {book}")
    def authenticate(self):
        u = cursor.execute("SELECT * FROM Users WHERE name = ?", (self.name,)).fetchall()
        passwd = u[0][3]
        if self.pwdhash == passwd:
            print("Authentication is successful!")
            return True
        return False
    def checkbooks(self):
        data = cursor.execute("SELECT * FROM Tx WHERE user = ?", (self.id,)).fetchall()
        for dag in data:
            if dag[2] == "Borrowed":
                self.Borrowed.append(dag)
            else:
                self.Bought.append(dag)
        return {"Bought": self.Bought, "Borrowed": self.Borrowed}
    def subscribe(duration):
        print("Function is not yet available")
    def unsubscribe():
        print("Function is not yet available!")

