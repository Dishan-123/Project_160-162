from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import webbrowser
from tkinter import messagebox

root = Tk()

root.minsize(650,650)
root.maxsize(650,650)
root.config(bg="orange")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
run_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label = Label(root, text="file name:")
label.place(relx=0.28, rely=0.03, anchor=CENTER)

inpu = Entry(root)
inpu.place(relx=0.046, rely=0.03, anchor=CENTER)

txt = Text(root, height=20, width=30, bg="aqua", fg="orange")
txt.place(relx=0.2, rely=0.3, anchor=CENTER)

name = ""

def openFile():
    global name
    
    txt.delete(1,END)
    inpu.delete(0,END)
    html_file = filedialog.askopenfilename(title = "Open HTML File", filetypes=(("Html Files", ".html"),))
    print(html_file)
    name = os.path.basename(html_file)
    
    formated_name = name.split('.')[0]
    inpu.insert(END, formated_name)
    root.title(formated_name)
    html_file = open(name, 'r')
    paragraph=html_file.read()
    txt.insert(END, paragraph)
    html_file = close(name, 'r')
    
def save():
    input_name = inpu.get()
    file = open(input_name+".html", "w")
    data = txt.get("1.0",END)
    print(data)
    file.write(data)
    inpu.delete(0, END)
    txt.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
    
def run_html_file():
    webbrowser.open(name)   
    
open_button = Button(root, image = open_img, text="Open File")
open_button.place(relx=0.05, rely=0.05, anchor=CENTER)

save_button = Button(root, image = save_img, text="Save File")
save_button.place(relx=0.15, rely=0.05, anchor=CENTER)

run_button = Button(root, image = run_img, text="Run File")
run_button.place(relx=0.23, rely=0.05, anchor=CENTER)