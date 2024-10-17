from tkinter import *
# from flames import *
import time

def loading():
    window=Tk()
    window.geometry("400x200")
    window.configure(bg="BLACK")
    icon=PhotoImage(file="Flames_App\App_images\icons8-heart-50.png")
    window.iconphoto(True,icon)
    window.title("FLAMES CALCULATOR")
    mainloop()

loading()
    
