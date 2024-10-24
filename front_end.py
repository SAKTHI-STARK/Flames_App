from tkinter import *
import tkinter as tk
from tkinter.font import Font
from flames import *
from gif_animation import AnimatedGIF
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
        show_result=""
        gif_label=""
       #function to communicate with backend
        def connection():
            value_1=Name_1_val.get()
            value_2=Name_2_val.get()
            result=back_end(value_1,value_2)
            result_font=Font(size=16,weight='bold')
            global show_result
            show_result=Label(window,text=result[0],bg="blanchedalmond",fg="deeppink3",font=result_font)
            show_result.place(x=120,y=210)
             # Create and place the GIF label
            global gif_label
            gif_label = AnimatedGIF(window,result[1])
            gif_label.place(x=200,y=250)
            AnimatedGIF(gif_label)
        #clear the entries and result in the window
        def clear():
                Name_1_val.delete(0,'end')
                Name_2_val.delete(0,'end')
                global show_result
                show_result.place_forget()
                global gif_label
                gif_label.place_forget()   
        #creating button to call function
        Button_calculate=Button(window,text="Find",fg="RED",command=connection)
        Button_calculate.place(x=300,y=160)
        Button_clear=Button(window,text="Clear",fg="RED",command=clear)
        Button_clear.place(x=340,y=160)
    main_window_elements()
#function for loading window
def loading():
    window.geometry("400x200")
    window.configure(bg="blanchedalmond")
    #icon for our app title
    icon=PhotoImage(file="Flames_App\\App_images\\icons8-heart-50.png")
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



    
