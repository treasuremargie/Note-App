from tkinter.filedialog import *
import tkinter as tk
 
canvas = tk.Tk()
canvas.geomery("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")

b1 = Button(canvas, text="Open", bg = "white")
b1.pack()

canvas.mainloop()