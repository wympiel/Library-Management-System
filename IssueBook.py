from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "******"  # wpisz swoje hasło
mydatabase = "library"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)

cur = con.cursor()  # cur -> cursor


# Enter Table Name here
issueTable = "books_issued"
bookTable = "books"

allBid = [] # To store all the Book ID's

def issue():

    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    laabelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()


    extractBid = "select bid from " +bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " +bookTable+ " where bid = '" +bid+ "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    