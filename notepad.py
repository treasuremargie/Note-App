from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode = 'w', filetypes = [('Text Files', '.txt')])
    if new_file is None:
        return
    text = entry.get(1.0, tk.END)
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode='r',filetypes=[('Text Files', '*.txt')] )
    if file is None:
        return
    content = file.read()
    entry.delete(1.0, tk.END)
    entry.insert(tk.INSERT, content)

    def clearFiles():
        entry.delete(1.0, tk.END)
        
canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="white") 

top = tk.Frame(canvas, bg="white")
top.pack(side=tk.TOP,anchor = 'nw',pady=5)

b1 = tk.Button(top, text="Open", bg="lightgray", command= openFile)
b1.pack(side=tk.LEFT, padx=5)

b2 = tk.Button(top, text="Save", bg="lightgray" , command = saveFile)
b2.pack(side=tk.LEFT, padx=5)

b3 = tk.Button(top, text="Clear", bg="lightgray", command= clearFile)
b3.pack(side=tk.LEFT, padx=5)

b4 = tk.Button(top, text="Exit", bg="lightgray", command = canvas.quit)
b4.pack(side=tk.LEFT, padx=5)

entry = tk.Text(canvas,wrap=tk.WORD,bg="#f9DDA4", font=("Poppins",15))
entry.pack(padx=10,pady=5,expand=True, fill=tk.BOTH)

canvas.mainloop()















