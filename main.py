from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
#from AdBook import *
#from DeleteBook import *
#from ViewBooks import *
#from IssueBook import *

mypass = "AmnFtlsQ58@"
mydatabase = "library"

con = pymysql.connect (host="localhost", user="root", password=mypass, database=mydatabase)


cur = con.cursor() # cur -> cursor

#window design
root = Tk()
root.title("Biblioteka")
root.minsize(width=400, height=400)
root.geometry("600x500")

same = True
n = 0.25

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300, 3400, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)
