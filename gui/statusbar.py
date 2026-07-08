from tkinter import Frame,Label
from config.theme import STATUS_BG

def create(parent):
    bar=Frame(parent,bg=STATUS_BG,height=24)
    Label(bar,text='Ready',bg=STATUS_BG,fg='white').pack(side='left',padx=8)
    return bar
