from tkinter import *
root = Tk()
root.title("Interactive Physics Quiz") #title
root.geometry("1200x800") #This is what defines the length and width of the application
root.resizable(False, False)

current_frame = None #starts of with the current frame being set as none (Used)

def switch_page(page_function): #Actts as variable for fage_function to do the work.
    global current_frame #allows us to change the variable to be present for all other parts of the code
    if current_frame is not None:
        current_frame.destroy() # Collapses the page 

    current_frame = tk.Frame(root) 
    current_frame.pack(fill="both", expand =True) #allows the fu
    page_function(current_frame)

def load_home(frame):
    label = tk.Label(frame, text="home", font=("Arial", 14))
    label.place(y=100, x=100)
    btn = tk.Button(frame, text="Go to Profile", command=lambda: switch_page(load_profile))
    btn.place(x=100, y=50)

def load_profile(frame):
    label = tk.Label(frame, text="Profile", font=("Arial", 14))
    label.place(y=200, x=200)
    btn = tk.Button(frame, text="Go to Home", command=lambda: switch_page(load_home))
    btn.place(x=200, y=150)


switch_page(load_home)
root.mainloop()
      


