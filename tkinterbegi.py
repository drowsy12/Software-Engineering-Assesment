from tkinter import *
import tkinter as tk
root = Tk()
root.title("Interactive Physics Quiz") #title
root.geometry("600x800") #This is what defines the length and width of the application
root.resizable(False, False)

current_frame = None #starts of with the current frame being set as none (Used)

def switch_page(page_function): #Actts as variable for fage_function to do the work.
    global current_frame #allows us to change the variable to be present for all other parts of the code
    if current_frame is not None:
        current_frame.destroy() # Collapses the page 

    current_frame = tk.Frame(root) 
    current_frame.pack(fill="both", expand =True) #allows the function to display the frame
    page_function(current_frame)

def load_home(frame):
    bg_image= tk.PhotoImage(file="/Users/mohammed/School/11SENG26/Software Engineering Assesment2/Software Engineering Assesment/Physics.png")
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = tk.Label(frame, text="Home Page", font=("Arial", 24, "bold"))
    title.place(x=150, y=50)
    label = tk.Label(frame, text="home", font=("Arial", 14))
    label.place(y=100, x=100)
    btn = tk.Button(frame, text="Go to Learning", command=lambda: switch_page(load_learning))
    btn.place(x=100, y=50)

def load_learning(frame):
    label = tk.Label(frame, text="Learn For Your quiz", font=("Arial", 14))
    label.place(y=200, x=200)
    btn = tk.Button(frame, text="Go to Home", command=lambda: switch_page(load_home))
    btn.place(x=200, y=150)
    btn = tk.Button(frame, text="Go to Home", command=lambda: switch_page(load_info1))
    btn.place(x=200, y=150)
    btn = tk.Button(frame, text="Back", command=lambda: switch_page(load_home))
    btn.place(x=200, y=150)

def load_info1(frame):
    label = tk.Label(frame, text="Learning", font=("Arial", 14))
    label.place(y=200, x=200)
    btn = tk.Button(frame, text="Go Back to Home", command=lambda: switch_page(load_home))
    btn.place(x=200, y=150)
    btn = tk.Button(frame, text="Back", command=lambda: switch_page(load_info1))
    btn.place(x=200, y=150)







switch_page(load_home)
root.mainloop()
      


