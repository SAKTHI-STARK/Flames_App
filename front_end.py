from tkinter import *
import tkinter as tk
from tkinter.font import Font
# from flames import *
import time
#function for the loading window of the app
# window=Tk()
window=tk.Tk()

def main_window(Name_app,author_name):
    #to dissapear existing text in the window
    Name_app.place_forget()
    author_name.place_forget()
    #to resize the loading window to main window
    window.geometry("600x400")
        
def loading():
    window.geometry("400x200")
    window.configure(bg="blanchedalmond")
    #icon for our app title
    icon=PhotoImage(file="Flames_App\App_images\icons8-heart-50.png")
    window.iconphoto(True,icon)
    window.title("FLAMES CALCULATOR")
    #creating name for our app name
    App_name_font=Font(size=30,weight='bold')
    App_name=tk.Label(window,text="FLAMES",bg="blanchedalmond",fg="deeppink4",font=App_name_font)
    App_name.place(x=110,y=65)
    #creating author name for our app
    Author_name_font=Font(size=10,weight='bold')
    author_name=tk.Label(window,text="by SAKTHI-STARK",bg="blanchedalmond",fg="deeppink4",font=Author_name_font)
    author_name.place(x=153,y=110)
    #transforming window to new size 
    window.after(1000,lambda:main_window(App_name,author_name))
    window.mainloop()
    
        
loading()


    
