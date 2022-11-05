from tkinter import *
from tkinter.ttk import Notebook
import tkinter.font
import sv_ttk
app = Tk()
app.geometry('300x10')
app.title('School Notes')

def initialize(subject,data): 
    app.geometry('300x400')
    def save(): return notes.get(1.0, "end-1c")
    def quit(): app.title('Saving & Closing...'); out = open('data/subject_data/'+subject.lower()+'.txt','w'); out.write(save()); out.close(); app.after(1000, app.quit)
    notebook = Notebook(app)
    notebook.pack(pady=10, expand=True)
    frame1 = Frame(notebook, width=400, height=280)
    frame2 = Frame(notebook, width=400, height=280)
    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)
    notebook.add(frame1, text=subject)
    notebook.add(frame2, text='Account')
    notes = Text(frame1, height = 250, width = 395, bg = "white", relief='solid', borderwidth=0, highlightthickness=0) 
    arial = tkinter.font.Font(family="Helvetica", size=13)
    notes.insert('0.0', data)
    notes.config(padx=15, pady=10, font=arial)
    notes.pack()
    accountFile = open('data/account_data/account.txt','r').readlines()
    accountString = ""
    for i in range(len(accountFile)): accountString += accountFile[i]
    accountLabel = Label(frame2, text=accountString)
    accountLabel.pack()
    app.protocol('WM_DELETE_WINDOW', quit)
    sv_ttk.set_theme("light")
    app.mainloop()
