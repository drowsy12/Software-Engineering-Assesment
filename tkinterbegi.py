from tkinter import *
import tkinter as tk
from tkinter import font
import turtle 

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
long_question_font = ("Chalkboard", 23, "bold")



def reset_score(): #This function is used to reset the score of the user
    global score, score_label
    score = 0
    if score_label:
        score_label.config(text="Score: " + str(score) + "/ 10")  # Update the score label

def disable_buttons(buttons): #This function is used to disable the buttons after the user selects an answer
    for button in buttons:
        button.config(state="disabled")


def correct(buttons): #This function is used to display the message correct answer and add to the score.
    global score, score_label
    score += 1
    if score_label:
        score_label.config(text="Score: " + str(score)+ "/ 10")  # Update the score label\
    label = tk.Label(root, text="Correct answer!", font=(subtitle_font), bg="#DBCBCB", fg="black")
    label.place(x=200, y=700)
    disable_buttons(buttons)


    label = tk.Label(root, text="Correct answer!", font=(subtitle_font), bg="#DBCBCB", fg="black")
    label.place(x=200, y=700)

def wrong(buttons): #This function is used to display the message wrong answer.
    global score, score_label
    score += 0
    label = tk.Label(root, text="Incorrect answer. Try again!", font=(subtitle_font), bg="#DBCBCB", fg="black")
    label.place(x=150, y=750)
    disable_buttons(buttons)



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
    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. J", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option4.place(x=350, y=400)
    buttons = [option1, option2, option3, option4]


  

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 2", width=10, height=3, fg="black", command=lambda: switch_page(load_question2))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=550)

def load_question2(frame):#This is the function for loading the question 2 page


    background_image(frame)

    label = tk.Label(frame, text="Question 2: \nWhat is the SI unit of acceleration?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

 
    
    option1 = tk.Button(frame, text="A. m/s^2", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. m/s", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. Watts", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Km/h^2", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option4.place(x=350, y=400)
    buttons = [option1, option2, option3, option4]
    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 3", width=10, height=3, fg="black", command=lambda: switch_page(load_question3))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=550)

def load_question3(frame):#This is the function for loading the question 3 page


    background_image(frame)

    label = tk.Label(frame, text="Question 3: \nAn object starts from rest and accelerates uniformly \nat 3.0 m/s² along a straight line. \nWhat is its displacement after 4.0 seconds?", font=(long_question_font), bg="#DBCBCB", fg="black" )
    label.place(y=100, x=0)

    option1 = tk.Button(frame, text="A. 6.0 m", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. 48.0 m", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. 12.0 m", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. 24.0 m", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option4.place(x=350, y=400)
    buttons = [option1, option2, option3, option4]

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 4", width=10, height=3, fg="black", command=lambda: switch_page(load_question4))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=550)

def load_question4(frame):#This is the function for loading the question 4 page


    background_image(frame)

    label = tk.Label(frame, text="Question 4: \nWhich of the following quantities is a scalar?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=20)

    
    option1 = tk.Button(frame, text="A. Speed", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. Acceleration", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. Velocity", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. Displacement", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option4.place(x=350, y=400)
    buttons = [option1, option2, option3, option4]

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 5", width=10, height=3, fg="black", command=lambda: switch_page(load_question5))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=550)


def load_question5(frame):#This is the function for loading the question 5 page
    background_image(frame)

    label = tk.Label(frame, text="Question 5: The area under a velocity-time (v-t) \ngraph represents which physical quantity?", font=(long_question_font), bg="#DBCBCB", fg="black" )
    label.place(y=80, x=20)

    vtgraph_image= tk.PhotoImage(file="/Users/mohammed/School/11SENG26/Software Engineering Assesment2/Software Engineering Assesment/vtgraph.png")
    vtgraph_label = tk.Label(frame, image=vtgraph_image)
    vtgraph_label.image = vtgraph_image  # Keep a reference to the image
    vtgraph_label.place(x=50, y=150)

    
    option1 = tk.Button(frame, text="A. Acceleration", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option1.place(x=100, y=450)
    option2 = tk.Button(frame, text="B. Displacement", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option2.place(x=100, y=550) 
    option3 = tk.Button(frame, text="C. Jerk", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=350, y=450) 
    option4 = tk.Button(frame, text="D. Velocity", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option4.place(x=350, y=550)
    buttons = [option1, option2, option3, option4]

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 6", width=10, height=3, fg="black", command=lambda: switch_page(load_question6))
    btn.place(x=400, y=650)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=650)

def load_question6(frame):#This is the function for loading the question 6 page


    background_image(frame)

    label = tk.Label(frame, text="Question 6: \n If you walk 4 meters East and then 3 meters North, \nwhat is the magnitude of your total displacement?", font=(long_question_font), bg="#DBCBCB", fg="black" )
    label.place(x=0, y=150)



    option1 = tk.Button(frame, text="A. 3.4 m", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. 12.0 m", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. 5.0 m", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. 7.0 m", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option4.place(x=350, y=400)
    buttons = [option1, option2, option3, option4]
    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 7", width=10, height=3, fg="black", command=lambda: switch_page(load_question7))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=550)

def load_question7(frame):#This is the function for loading the question 7 page


    background_image(frame)

    label = tk.Label(frame, text="Question 7: \nA rock is dropped from a bridge. \nWhat is its acceleration  2 seconds into the fall?", font=(long_question_font), bg="#DBCBCB", fg="black" )
    label.place(y=180, x=20)

    
    option1 = tk.Button(frame, text="A. 9.8 m/s^2", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. 9.8 m/s", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. 0 m/s^2", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. 19.8 m/s^2", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option4.place(x=350, y=400)
    buttons = [option1, option2, option3, option4]
    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 8", width=10, height=3, fg="black", command=lambda: switch_page(load_question8))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=550)

def load_question8(frame):#This is the function for loading the question 8 page


    background_image(frame)

    label = tk.Label(frame, text="Question 8: \nDuring which time interval\n is the object experiencing an acceleration of 0?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=60, x=0)

    vtgtwo = tk.PhotoImage(file="/Users/mohammed/School/11SENG26/Software Engineering Assesment2/Software Engineering Assesment/image_5d2fc4b7.png")
    vtgtwo = vtgtwo.subsample(3, 3)  # Resize the image to half its original size
    vgtwo_label = tk.Label(frame, image=vtgtwo)
    vgtwo_label.image = vtgtwo  # Keep a reference to the image
  
    vgtwo_label.place(x=65, y=170)

 
    option1 = tk.Button(frame, text="A. 0 to 2 seconds", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option1.place(x=100, y=450)
    option2 = tk.Button(frame, text="B. 6 to 8 seconds", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option2.place(x=100, y=550) 
    option3 = tk.Button(frame, text="C. 4 to 6 seconds", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=350, y=450) 
    option4 = tk.Button(frame, text="D. 2 to 4 seconds", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option4.place(x=350, y=550)
    buttons = [option1, option2, option3, option4]

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 9", width=10, height=3, fg="black", command=lambda: switch_page(load_question9))
    btn.place(x=400, y=650)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=650)
    
def load_question9(frame):#This is the function for loading the question 9 page


    background_image(frame)

    label = tk.Label(frame, text="Question 9: \nIf A bicycle travels a distance of 15m in 3s \nWhat is its speed?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=160, x=40)

    
    option1 = tk.Button(frame, text="A. 5 m/s", font=(button_font), width=10, height=3, fg="black", command=lambda: correct(buttons))
    option1.place(x=100, y=300)
    option2 = tk.Button(frame, text="B. 9 m/s", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option2.place(x=100, y=400) 
    option3 = tk.Button(frame, text="C. 4 m/s", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=350, y=300) 
    option4 = tk.Button(frame, text="D. 2 m/s", font=(button_font), width=10, height=3, fg="black", command=lambda: wrong(buttons))
    option4.place(x=350, y=400)
    buttons = [option1, option2, option3, option4]

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to question 10", width=10, height=3, fg="black", command=lambda: switch_page(load_question10))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=550)

def load_question10(frame):#This is the function for loading the question 10 page
    background_image(frame)

    label = tk.Label(frame, text="Question 10:\n What is the main difference between\n speed and velocity?", font=(subtitle_font), bg="#DBCBCB", fg="black" )
    label.place(y=160, x=85)


    
    option1 = tk.Button(frame, text="A. Speed includes a direction,\n but velocity does not.", font=(button_font), width=20, height=3, fg="black", command=lambda: wrong(buttons))
    option1.place(x=40, y=300)
    option2 = tk.Button(frame, text="B. Velocity and speed both include\n direction and magnitude.", font=(button_font), width=20, height=3, fg="black", command=lambda: wrong(buttons))
    option2.place(x=40, y=400) 
    option3 = tk.Button(frame, text="C. They mean the\n exact same thing", font=(button_font), width=20, height=3, fg="black", command=lambda: wrong(buttons))
    option3.place(x=320, y=300) 
    option4 = tk.Button(frame, text="D.Velocity includes a direction,\n but speed does not.", font=(button_font), width=20, height=3, fg="black", command=lambda: correct(buttons))
    option4.place(x=320, y=400)
    buttons = [option1, option2, option3, option4]

    score_display(frame)

    btn = tk.Button(frame, font=button_font, text="Go to Results", width=10, height=3, fg="black", command=lambda: switch_page(load_results))
    btn.place(x=400, y=550)
    btn = tk.Button(frame, font=button_font, text="Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=100, y=550)

def load_results(frame):#This is the function for loading the results page
    background_image(frame)

    label = tk.Label(frame, text="Results", font=(title_font), bg="#DBCBCB", fg="black" )
    label.place(y=200, x=100)

    score_label = tk.Label(frame, text="Your Score: " + str(score) + "/10", font=(subtitle_font), bg="#DBCBCB", fg="black")
    score_label.place(y=300, x=100)

    btn = tk.Button(frame, font=button_font, text="Back to Home", width=10, height=3, fg="black", command=lambda: switch_page(load_home))
    btn.place(x=400, y=550)
    reset_btn = tk.Button(frame, font=button_font, text="Reset Score", width=10, height=3, fg="black", command=reset_score)
    reset_btn.place(x=100, y=550)
    
switch_page(load_home)
root.mainloop()