from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "******"  # wpisz swoje hasło
mydatabase = "library"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)

cur = con.cursor()  # cur -> cursor

# Enter Table Names here
issueTable = "books_issued"
bookTable = "books"

allBid = []  # To store all Book ID's

def return():

    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    bid = bookInfo1.get()

    extractBid = "select bid from " +issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in allBid:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " +bookTable+ "where bid = '" +bid+ "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo()