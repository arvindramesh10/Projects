from tkinter import *

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("Calculator")
window.geometry("500x500")
icon = PhotoImage(file='Calc_Logo.png')
window.iconphoto(True,icon)

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('/', 3, 3),
]

for (text, row, column) in buttons:
    Button(frame, text=text, height=4, width=9, font=35, command=lambda t=text: button_press(t) if t != '=' else equals()).grid(row=row, column=column)

clear_button = Button(window, text='clear', height=4, width=12, font=35, command=clear)
clear_button.pack()

window.mainloop()