from tkinter import *
import tkinter as tk
from tkinter import font 

root = Tk()
root.title("Interactive Physics Quiz") #title
root.geometry("600x800") #This is what defines the length and width of the application
root.resizable(False, False)

#Defining the fonts and using the corrcr font
title_font = ("Chalkboard", 60, "bold" )
subtitle_font =("Chalkboard", 16,)
button_font_font =("Chalkboard", 16, "bold")
button_font = ("Chalkboard", 20 )

current_frame = None #starts of with the current frame being set as none

def switch_page(page_function): #Actts as variable for fage_function to do the work.
    global current_frame #allows us to change the variable to be present for all other parts of the code
    if current_frame is not None:
        current_frame.destroy() # Collapses the page 

    current_frame = tk.Frame(root) 
    current_frame.pack(fill="both", expand =True) #allows the function to display the frame
    page_function(current_frame)

def load_home(frame):
    bg_image= tk.PhotoImage(file="/Users/mohammed/School/11SENG26/Software Engineering Assesment2/Software Engineering Assesment/Physics (600 x 800 px).png")
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(relwidth=1, relheight=1)

    title = tk.Label(root, text="Physics Quiz", font=title_font, bg="#DBCBCB")
    title.place(x=100, y=170)
    btn = tk.Button(frame, font=button_font, text="Go to \n Learning", width=5, height=3, fg="#DBCBCB", command=lambda: switch_page(load_learning))

    btn.place(x=400, y=300)

def load_learning(frame):

    bg_image= tk.PhotoImage(file="/Users/mohammed/School/11SENG26/Software Engineering Assesment2/Software Engineering Assesment/Physics (600 x 800 px)-2.png")
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(relwidth=1, relheight=1)


    label = tk.Label(frame, text="Learn For Your quiz", font=("Arial", 14))
    label.place(y=200, x=200)
    btn = tk.Button(frame, text="Go to Home", command=lambda: switch_page(load_home))
    btn.place(x=200, y=150)
    btn = tk.Button(frame, text="Go to Home", command=lambda: switch_page(load_info1))
    btn.place(x=200, y=150)
    btn = tk.Button(frame, text="Back", command=lambda: switch_page(load_home))
    btn.place(x=200, y=150)

def load_info1(frame):


    bg_image= tk.PhotoImage(file="/Users/mohammed/School/11SENG26/Software Engineering Assesment2/Software Engineering Assesment/Physics (600 x 800 px)-2.png")
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(relwidth=1, relheight=1)

    label = tk.Label(frame, text="Learning", font=("Arial", 14))
    label.place(y=200, x=200)
    btn = tk.Button(frame, text="Go Back to Home", command=lambda: switch_page(load_home))
    btn.place(x=200, y=150)
    btn = tk.Button(frame, text="Back", command=lambda: switch_page(load_info1))
    btn.place(x=200, y=150)







switch_page(load_home)
root.mainloop()
      


