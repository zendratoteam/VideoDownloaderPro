from tkinter import Frame,Entry,Button
def create(parent):
 f=Frame(parent)
 e=Entry(f)
 e.pack(side='left',fill='x',expand=True,padx=5,pady=5)
 Button(f,text='Analyze').pack(side='left',padx=5)
 return f
