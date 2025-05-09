import tkinter

from tkinter import *

ui = tkinter.Tk()
ui.title("BMI Calculator")
ui.configure(background= "blue")
ui.geometry("300x300")
result = tkinter.Label(ui, background="blue", width=50, height=1)
result.pack(side="bottom", pady=5, anchor="center")

def calculate():
    weight = (w_entry.get())
    height = (h_entry.get())

    if (weight == "" or height == ""):
        result.config(text= "Enter both weight and height!")
        return

    try:
        finalWeight = ((float)(w_entry.get()))
        finalHeight = ((float)(h_entry.get()) / 100)
    except:
        result.config(text= "Enter a valid number!")

    if (finalWeight <= 0):
        result.config(text= "Invalid weight")
        return

    if (finalHeight <= 0):
        result.config(text= "Invalid height")
        return

    BMI = finalWeight / (finalHeight * finalHeight)

    if (BMI < 18.5):
        result.config(text= f"Your BMI is: {round(BMI,2)}, You are Underweight")
    elif (18.5 <= BMI <= 24.9):
        result.config(text= f"Your BMI is: {round(BMI,2)}, You are Normal")
    elif (25 <= BMI <= 39.9):
        result.config(text= f"Your BMI is: {round(BMI,2)}, You are Overweight")
    elif (40 <= BMI):
        result.config(text= f"Your BMI is: {round(BMI,2)}, You are Obese")

w_label = tkinter.Label(ui,background= "blue",text= "Enter your weight (kg)",width= 30,height= 1)
w_label.pack(side="top",pady=5,anchor="center")
w_label.configure(foreground= "black")
w_entry = tkinter.Entry(ui)
w_entry.pack(side="top",pady=5,anchor="center")
h_label = tkinter.Label(ui,background= "blue",text= "Enter your height (cm)",width= 30,height= 1)
h_label.pack(side="top",pady=5,anchor="center")
h_label.configure(foreground= "black")
h_entry = tkinter.Entry(ui)
h_entry.pack(side="top",pady=5,anchor="center")
calculate = tkinter.Button(text= "Calculate",command=calculate)
calculate.pack(side="top",pady=5,anchor="center")
calculate.configure(foreground= "black")
w_entry.focus()

ui.mainloop()