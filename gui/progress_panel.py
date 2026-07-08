from tkinter import Frame,Label
from tkinter.ttk import Progressbar

def create(parent):
 f=Frame(parent,bd=1,relief='groove',padx=10,pady=10);Label(f,text='Download Progress').pack(anchor='w');Progressbar(f,length=500).pack(fill='x',pady=8);Label(f,text='0% | Waiting').pack(anchor='w');return f