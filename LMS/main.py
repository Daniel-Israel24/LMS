from backend import *
import random
user_id = None
def dash():
    print("\n\n")
    print("="*100)
    print("Welcome to G3 Library!")
    print("How can we help you?\nPlease choose a service from the list:")
    print("1. View available books\n2. Borrow a book\n3. Buy a book\n4. Return a borrowed book.\n5. Check my books\n6. Sign Out\n7. Exit")
    option = input("Choose the operation: ")
    match option:
        case "1":
            SeeBooks()
        case "2":
            BorrowBook()
        case "3":
            BuyBook()
        case "4":
            ReturnBook()
        case "5":
            CheckMyBooks()
        case "6":
            global user_id
            user_id = None
            print("Successfully signed out!")
            print("="*102)
            main()
        case "7":
            dbase.close()
            print("Thank you for visiting the G3Library!")
            exit()

def SeeBooks():
    print("Hello These are the available books in our library as at now!")
    dat = cursor.execute("SELECT * FROM Books").fetchall()
    print("_"*100)
    print("ISBN\t\tTitle\t\t\tAuthor\t\tPublisher\t\tPrice\t\tCopies")
    print("_"*100)
    for data in dat:
        print("\n")
        for p in data:
            print(f"{p}\t\t", end="")
    print("\n")
    print("_"*100)
def BorrowBook():
    print("Hello, you have opted to borrow a book.")
    SeeBooks()
    global user_id
    isbn = int(input("Enter the ISBN of the book you want: "))
    # Then register the transaction to the Tx table
    cursor.execute("INSERT INTO Tx (user, book, txType, completed) VALUES (?, ?, ?, ?)", (user_id, isbn, "Borrow", 0))
    dbase.commit()
    print(f"Successfully borrowed the book {isbn}")
def BuyBook():
    print("Hello, You have opted to buy a book.")
    SeeBooks()
    global user_id
    isbn = int(input("Enter the ISBN of the book you want: "))
    # Then register the transaction to the Tx table.
    cursor.execute("INSERT INTO Tx (user, book, txType, completed) VALUES (?, ?, ?, ?)", (user_id, isbn, "Bought", 0))
    dbase.commit()
    print("This Function is still under development!")
def ReturnBook():
    print("You are in the process of returning a book.\nHope this book has helped you in the intended purpose.")
    isbn = input("Enter the ISBN of the book you want to return: ")

def CheckMyBooks():
    print("Function is yet to be developed!")
    d = cursor.execute("SELECT * FROM Tx WHERE user = ?", (user_id,)).fetchall()
    borrowed = []
    bought = []
    for da in d:
        if da[2] == "Borrow":
            borrowed.append(da[1])
        else:
            bought.append(da[1])
    
    return borrowed, bought
def authenticate(user):
    u = cursor.execute("SELECT * FROM Users WHERE name = ?", (user,)).fetchall()
    global user_id
    if len(u):
        usr = u[0][1]
        print(f"Welcome back {usr}!")
        user_id = u[0]
        pwd = input("Please enter your password: ")
        cusr = User(user_id, user, pwd, 0)
        if cusr.authenticate():
            return True
        else:
            for i in range(3):
                pwd = input("Incorrect password! Please try again: ")
                cusr = User(user_id, user, pwd, 0)
                if cusr.authenticate():
                    return True
            print("You tried incorrect password 4 times. Authentication terminated!")
            del cusr
            user_id = None
            main()
    print("The user Does not exist! Please try another.")
    return False
    
def SignUp(uname, pwd):
    nuser = User(random.randint(1, 50000), uname, False, pwd)
    nuser.save()
def main():
    shouldClose = False
    while not user_id:
        print("Welcome to G3 library!\n")
        print("Please choose an option.\n    1. Log In\n    2. Sign Up\n    3. Exit")
        c = input("Choose an option: ")
        match c:
            case "1":
                user = input("Enter your user name: ")
                if not authenticate(user):
                    print("Authentication Failed!")
            case "2":
                user = input("Enter your desired user name: ")
                pswd = input("Enter your password: ")
                SignUp(user, pswd)
            case "3":
                dbase.close()
                exit()
    while not shouldClose:
        dash()
main()
    