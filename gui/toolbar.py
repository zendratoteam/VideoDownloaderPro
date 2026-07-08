from tkinter import Frame,Button
from config.theme import TOOLBAR_BG
def create(parent):
 f=Frame(parent,bg=TOOLBAR_BG,height=44)
 for t in ['Paste URL','Analyze','Download','Stop','Open Folder']:
  Button(f,text=t).pack(side='left',padx=4,pady=5)
 return f
