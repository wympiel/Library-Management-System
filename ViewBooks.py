from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

mypass = "******"  # wpisz swoje hasło
mydatabase = "library"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)

cur = con.cursor()  # cur -> cursor

# Enter table names here
bookTable = "books"


def View():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#ffbb00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg="white", font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    