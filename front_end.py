from tkinter import *
import tkinter as tk
from tkinter.font import Font
# from flames import *
import time
#function for the loading window of the app
def loading():
    window=Tk()
    window.geometry("400x200")
    window.configure(bg="blanchedalmond")
    #icon for our app title
    icon=PhotoImage(file="Flames_App\App_images\icons8-heart-50.png")
    window.iconphoto(True,icon)
    window.title("FLAMES CALCULATOR")
    #creating name for our app name
    Name_app_font=Font(size=30,weight='bold')
    Name_app=tk.Label(window,text="FLAMES",bg="blanchedalmond",fg="deeppink4",font=Name_app_font)
    Name_app.place(x=110,y=65)
    #creating author name for our app
    Author_name_font=Font(size=10,weight='bold')
    author_name=tk.Label(window,text="by SAKTHI-STARK",bg="blanchedalmond",fg="deeppink4",font=Author_name_font)
    author_name.place(x=153,y=110)
    
    
    mainloop()

loading()
    
