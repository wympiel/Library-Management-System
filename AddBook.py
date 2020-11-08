from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = status.lower()

    insertBooks = "insert into" + bookTable + "values('" + bid + "', '" + title + "', '" + author + "', '" + status + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database.")

    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()


def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")


    mypass = "root"
    mydatabase = "library"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
