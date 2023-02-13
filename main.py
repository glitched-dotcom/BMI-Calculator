# importing tkinter for the GUI window
import tkinter as Tk
from tkinter import *

# creating our function that will do all the heavy lifting for our BMI calculator
def generate():
    weight = int(w1.get())
    height = int(h1.get())

    # this is our function that takes the inputted values from the user and calculates their BMI value
    BMI = float((weight / (height/100) ** 2))

    # we'll use an if else statement to deal with different weight and height inputs
    if BMI < 18.5:
        text_output.set(f'You are underweight')
    elif BMI >= 18.6 and BMI <= 24.9:
        text_output.set(f'You have a normal weight')
    elif BMI >= 25.0 and BMI <= 29.9:
        text_output.set(f'You are overweight')
    elif BMI >= 30.0:
        text_output.set(f'You are obese') 
    
    # prints out the final BMI value for the user
    num_output.set(BMI)

# using tkinter to create a simple GUI (graphical user interface) for the user to see
window = Tk()
window.title("BMI Calculator")
window.geometry("600x400")

# using intvar for our integer values (height and weight)
# stringvar to display the weight group a user would be in
# doublevar for the bmi index output
# using these so the data in the variables can be displayed into the GUI textboxes
weight = IntVar()
height = IntVar()
text_output = StringVar()
num_output = DoubleVar()

# labels are to show what should be inputted into where and where specific data is going to be displayed
L1 = Label(window, text='Please input Weight in (kg)')
L1.place(x=50, y=50)

L2 = Label(window, text='Please input Height in (cm)')
L2.place(x=50, y=150)

L3 = Label(window, text='Your Body Mass Idex (BMI) is', bd=2)
L3.place(x=40, y=250)

L4 = Label(window, text='Overall', bd=2)
L4.place(x=175, y=212)

# here are the variables and entry boxes that take our inputted data and display them to the user in the GUI box
w1 = Entry(window, textvariable=weight, bd=2)
w1.place(x=229, y=48)

h1 = Entry(window, textvariable=height, bd=2)
h1.place(x=229, y=148)

text = Entry(window, textvariable=text_output, bd=2)
text.place(x=229, y=210)

num = Entry(window, textvariable=num_output, bd=2)
num.place(x=229, y=248)

# button that executes the function and gives us our output
b = Button(window, text='Calculate BMI')
b.configure(text='Calculate', command=generate)
b.place(x=270, y=350)

# keeps the window open until we manually close it ourselves
window.mainloop()