from tkinter import *
import tkinter as tk
from tkinter.font import Font
from flames import *
#function for the loading window of the app
window=tk.Tk()
#function for the main window
def main_window(Name_app,author_name):
    #to dissapear existing text in the window
    Name_app.place_forget()
    author_name.place_forget()
    #to resize the loading window to main window
    window.geometry("600x400")
    def main_window_elements():
        #display flames calculator in the main window
        Header_font=Font(size=22,weight='bold')
        Header=tk.Label(window,text="FLAMES CALCULAT💘R",bg="blanchedalmond",fg="deeppink4",font=Header_font)
        Header.place(x=150,y=20)
        #labels to get show what to do Name_1 
        Name_1=tk.Label(window,text="Your Name",bg="blanchedalmond",fg="black")
        Name_1.place(x=180,y=80)
        Name_1_val=tk.Entry()
        Name_1_val.place(x=260,y=80,width=200)
        #labels to get show what to do Name_2
        Name_2=tk.Label(window,text="Crush Name",bg="blanchedalmond",fg="black")
        Name_2.place(x=180,y=110)
        Name_2_val=tk.Entry()
        Name_2_val.place(x=260,y=110,width=200)
        #function to communicate with backend
        def connection():
            value_1=Name_1_val.get()
            value_2=Name_2_val.get()
            result=back_end(value_1,value_2)
            print(result)
        #creating button to call function
        Button_calculate=Button(window,text="FIND",fg="RED",command=connection)
        Button_calculate.place(x=300,y=160)
    main_window_elements()
#function for loading window
def loading():
    window.geometry("400x200")
    window.configure(bg="blanchedalmond")
    #icon for our app title
    icon=PhotoImage(file="App_images\icons8-heart-50.png")
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
    window.after(700,lambda:main_window(App_name,author_name))
    window.mainloop()
loading()



    
