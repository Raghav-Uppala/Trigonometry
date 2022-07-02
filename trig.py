from ctypes import windll
from tkinter import ttk
from tkinter import *
import random

#fixing the windows blur bug
windll.shcore.SetProcessDpiAwareness(1)

#Setting up the window
root = Tk()
root.title("Trigonometry test")
# root.iconbitmap('./icondir/icon.ico')
# root.resizable(0, 0)
# root.attributes('-alpha', 0.9)
# root.attributes('-topmost', 1)
window_width = 825
window_height = 700

#Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

#Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


#------------------------------- Cross page setup

questions = ["Question 1", "Question 2","Question 3", "Question 4", "Question 5"]
answers = ["Answer 1","Answer 2", "Answer 3", "Answer 4", "Answer 5"]

def switch_to(frame):
    frame.tkraise()


index_page = Frame(root)
question_page = Frame(root)
test_page = Frame(root)
# f3 = Frame(root)
# f4 = Frame(root)

for frame in (index_page, test_page, question_page):
    frame.grid(row=0, column=0, sticky="news")
#------------------------------- Index Page

#functions


#Initializing the Widgets
start_btn = ttk.Button(index_page)
show_questions_btn = ttk.Button(index_page)

#Configs
start_btn["text"] = "Start Test"
start_btn["command"] = lambda: switch_to(test_page)

show_questions_btn["text"] = "Show Questions"
show_questions_btn["command"] = lambda: switch_to(question_page)

#binds


#Packing the Widgets
start_btn.pack()
show_questions_btn.pack()

#------------------------------- Questions Page

#------------------------------- Test Page

#functions
def sub_btn_submit(event):
    print(event)

def random_question():
  return questions[random.randint(0, len(questions)-1)]

#Initializing the Widgets
question_display = ttk.Label(test_page)
sub_btn = ttk.Button(test_page)

#Configs
question_display["text"] = random_question()
sub_btn["text"] = "Submit"
sub_btn["command"] = lambda: switch_to(index_page)

#binds
sub_btn.bind('<space>', sub_btn_submit)
sub_btn.bind('<Return>', sub_btn_submit, add='+')

#Packing the Widgets
question_display.pack()
sub_btn.focus()
sub_btn.pack()

#-------------------------------

switch_to(index_page)
root.mainloop()
