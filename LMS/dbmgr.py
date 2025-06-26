# This module is basically to populate the database with sample data
"""
The database has 3 tables:
Users: (id, name, staff, passwd)
Tx: (user, book, txType, completed)
Books: (isbn, title, author, publisher, price, copies)
"""
import backend as be
be.initdb()
books = [
    [1001, "Python 101", "Mike", "CodePress", 29, 5],
    [1002, "Learn SQL", "Sara", "DataBooks", 25, 3],
    [1003, "C++ Basics", "John", "CodePress", 37, 4],
    [1004, "HTML & CSS", "Tina", "WebStart", 20, 6],
    [1005, "Flask Web Dev", "Anna", "CodePress", 28, 2],
    [1006, "Data Science", "Leo", "MathWorld", 40, 5],
    [1007, "Java in Depth", "Raj", "Techie", 33, 4],
    [1008, "OS Concepts", "Ken", "UniPub", 42, 3],
    [1009, "Linux Basics", "Amila", "Techie", 23.75, 7],
    [1010, "AI Starter", "Eli", "SmartBooks", 45, 20]
]
users = [
    [1, "Alice", 1, "alice123"],
    [2, "Bob", 0, "bobpass"],
    [3, "Clara", 1, "clarapwd"],
    [4, "Dan", 0, "d4nword"],
    [5, "Eve", 0, "eve!eve"]
]
print("Fingers crossed, awaiting if the code will run successfully")
for book in books:
    bk = be.Book(book[1], book[0], book[2], book[3], book[4],book[5])
    try:
        bk.add()
    except:
        print(f"Failed to add book {book[0]}")
        continue
for user in users:
    us = be.User(user[0], user[1], user[3], user[2])
    us.save()
print("Code has run without errors!")