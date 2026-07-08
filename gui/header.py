from tkinter import Frame,Label
from config.theme import HEADER_BG,TITLE_FONT
from config.config import APP_NAME,APP_VERSION
def create(parent):
 f=Frame(parent,bg=HEADER_BG,height=56)
 f.pack_propagate(False)
 Label(f,text=f'{APP_NAME}  {APP_VERSION}',bg=HEADER_BG,fg='white',font=TITLE_FONT).pack(side='left',padx=12)
 return f
