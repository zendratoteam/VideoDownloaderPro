from tkinter import Frame,Button
from config.theme import SIDEBAR_BG
def create(parent):
 f=Frame(parent,bg=SIDEBAR_BG,width=220);f.pack_propagate(False)
 items=['Home','Downloads','History','Settings','About']
 for i in items:
  Button(f,text=i,anchor='w').pack(fill='x',padx=8,pady=3)
 return f
