import tkinter as tk
from tkinter import messagebox

# Function to update the input field
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        current = screen.get()
        screen.set(current + text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Input field
screen = tk.StringVar()
input_field = tk.Entry(root, textvar=screen, font="Arial 18", bd=8, relief=tk.RIDGE, justify="right")
input_field.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create and place buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH)
    for btn_text in row:
        button = tk.Button(
            frame, text=btn_text, font="Arial 18", relief=tk.RIDGE, height=2, width=4, bd=2
        )
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        button.bind("<Button-1>", click)

# Run the application
root.mainloop()
