from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "******" # wpisz swoje hasło
mydatabase = "library"

con = pymysql.connect (host="localhost", user="root", password=mypass, database=mydatabase)


cur = con.cursor() # cur -> cursor

# Enter Table Name here
issueTable = "books_issued"
bookTable = "books" # Book Table

def deleteBook():

    bid = bookInfo1.get()

    deleteSql = "delete from " +bookTable+ "where bid = '" +bid+ "'"
    deleteIssue = "delete from " +issueTable+ " where bid = '" +bid+ "'"

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()

        messagebox.showinfo('SAuccess', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()

def delete():

    global  bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")


    