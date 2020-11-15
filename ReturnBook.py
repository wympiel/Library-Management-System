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
        messagebox.showinfo("Error", "Can't fetch Book ID's")

    issueSql = "delete from" +issueTable+ "where bid = '" +bid+ "'"

    print(bid in  allBid)
    print(status)
    updateStatus = "update " +bookTable+ "set status = 'avail' where bid = '" +bid+ "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Plkease check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong. Try again")

    allBid.clear()
    root.destroy()

def returnBook():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006b38")
    Canvas1.pack(expand=True, fill=BOTH)
    