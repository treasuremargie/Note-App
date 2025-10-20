from tkinter.filedialog import *
import tkinter as tk
canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="white")
top = tk.Frame(canvas, bg="white")
top.pack(side=tk.TOP,fill=tk.X,pady=5)
b1 = tk.Button(top, text="Open", bg="lightgray")
b1.pack(side=tk.LEFT, padx=2)
b2 = tk.Button(top, text="Save", bg="lightgray")
b2.pack(side=tk.LEFT, padx=2)
b3 = tk.Button(top, text="Clear", bg="lightgray")
b3.pack(side=tk.LEFT, padx=2)
b4 = tk.Button(top, text="Exit", bg="lightgray")
b4.pack(side=tk.LEFT, padx=2)
entry = tk.Text(canvas,wrap=tk.WORD,bg=)
canvas.mainloop()















