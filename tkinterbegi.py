from tkinter import *
import tkinter as tk
from tkinter import font 

root = Tk()
root.title("Interactive Physics Quiz") #title
root.geometry("600x800") #This is what defines the length and width of the application
root.resizable(False, False)
score = 0 #This is the score variable that will be used to keep track of the score of the user
score_label = None #This is the score label that will be used to display the score of the user

#Defining the fonts and using the corrcr font
title_font = ("Chalkboard", 60, "bold" )
subtitle_font =("Chalkboard", 25, "bold")
button_font =("Chalkboard", 16, "bold")



def correct():
    global score, score_label
    score += 1
    if score_label:
        score_label.config(text="Score: " + str(score)+ "/ 10")  # Update the score label
    
def wrong():
    global score
    score += 0


def background_image(frame): #This function is used to set the background image for the application
    bg_image= tk.PhotoImage(file="/Users/mohammed/School/11SENG26/Software Engineering Assesment2/Software Engineering Assesment/Physics (600 x 800 px)-2.png")
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(relwidth=1, relheight=1)

def score_display(frame): #This function is used to display the score of the user
    global score_label
    score_label = tk.Label(frame, text="Score: " + str(score), font=(subtitle_font), bg="#DBCBCB")
    score_label.place(x=10, y=10)


current_frame = None #starts of with the current frame being set as none

def switch_page(page_function): #Actts as variable for fage_function to do the work.
    global current_frame #allows us to change the variable to be present for all other parts of the code
    if current_frame is not None:
        current_frame.destroy() # Collapses the page 

    current_frame = tk.Frame(root) 
    current_frame.pack(fill="both", expand =True) #allows the function to display the frame
    page_function(current_frame)

def load_home(frame):#This part of the function is used for the homepage only.
    bg_image= tk.PhotoImage(file="/Users/mohammed/School/11SENG26/Software Engineering Assesment2/Software Engineering Assesment/Physics (600 x 800 px).png")
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to the image
    bg_label.place(relwidth=1, relheight=1)

    title = tk.Label(root, text="Physics Quiz", font=title_font, bg="#DBCBCB")
    title.place(x=100, y=170)
    btn = tk.Button(frame, font=button_font, text="Go to Quiz", width=20, height=3, fg="black", command=lambda: switch_page(load_quiz))
    btn.place(x=180, y=350)

def load_quiz(frame):#This part of the function is where the quiz is described and criterias for learning are set.

    background_image(frame)


    label = tk.Label(frame, text="This quiz has 10 multiple choice questions,\n which will test your understanding \nof basic Kinematic topics such as:\n Vecotrs  \nSUVATS\nGraphs  ", font=(subtitle_font), bg="#DBCBCB", fg="black" ) 
    label.place(y=250, x=50)
    btn = tk.Button(frame, font=button_font, text="Go to question 1", width=10, height=3, fg="black", command=lambda: switch_page(load_question1))
    btn.place(x=400, y=500)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=500)

def load_question1(frame):#This is the function for loading the question 1 page


    background_image(frame)

    label = tk.Label(frame, text="Question 1: \nWhat is the SI unit of velocity?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    answer = tk.StringVar() #This is the variable that will be used to store the answer of the user(Found from youtube video in reference link during the report)
    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question2))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_quiz))
    btn.place(x=100, y=550)

def load_question2(frame):#This is the function for loading the question 2 page


    background_image(frame)

    label = tk.Label(frame, text="Question 2: \nWhat is the SI unit of acceleration?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    answer = tk.StringVar() #This is the variable that will be used to store the answer of the user(Found from youtube video in reference link during the report)
    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=correct)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. Watts", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 3", width=10, height=3, fg="black", command=lambda: switch_page(load_question3))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_question1))
    btn.place(x=100, y=550)

def load_question3(frame):#This is the function for loading the question 3 page


    background_image(frame)

    label = tk.Label(frame, text="Question 3: \nWhat is the SI unit of force?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 4", width=10, height=3, fg="black", command=lambda: switch_page(load_question4))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_question2))
    btn.place(x=100, y=550)

def load_question4(frame):#This is the function for loading the question 4 page


    background_image(frame)

    label = tk.Label(frame, text="Question 4: \nWhat is the SI unit of energy?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question5))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_quiz))
    btn.place(x=100, y=550)


def load_question5(frame):#This is the function for loading the question 5 page
    background_image(frame)

    label = tk.Label(frame, text="Question 5: \nWhat is the SI unit of power?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question6))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_quiz))
    btn.place(x=100, y=550)

def load_question6(frame):#This is the function for loading the question 6 page


    background_image(frame)

    label = tk.Label(frame, text="Question 6: \nWhat is the SI unit of pressure?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question7))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_quiz))
    btn.place(x=100, y=550)

def load_question7(frame):#This is the function for loading the question 7 page


    background_image(frame)

    label = tk.Label(frame, text="Question 7: \nWhat is the SI unit of work?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question8))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_quiz))
    btn.place(x=100, y=550)

def load_question8(frame):#This is the function for loading the question 8 page


    background_image(frame)

    label = tk.Label(frame, text="Question 8: \nWhat is the SI unit of energy?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

 
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question9))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_quiz))
    btn.place(x=100, y=550)
    
def load_question9(frame):#This is the function for loading the question 9 page


    background_image(frame)

    label = tk.Label(frame, text="Question 9: \nWhat is the SI unit of power?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question10))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_question8))
    btn.place(x=100, y=550)

def load_question10(frame):#This is the function for loading the question 10 page
    background_image(frame)

    label = tk.Label(frame, text="Question 1: \nWhat is the SI unit of velocity?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)


    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=correct)
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=wrong)
    option4.place(x=350, y=400)

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question2))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Back", width=10, height=3, fg="black", command=lambda: switch_page(load_quiz))
    btn.place(x=100, y=550)
    
switch_page(load_home)
root.mainloop()