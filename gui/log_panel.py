from tkinter import Frame,Text

def create(parent):
    f=Frame(parent,bd=1,relief='groove')
    t=Text(f,height=8)
    t.insert('end','Application log...\n')
    t.pack(fill='both',expand=True,padx=5,pady=5)
    return f
