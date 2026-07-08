import tkinter as tk

def create_menu(root):
 m=tk.Menu(root);root.config(menu=m);fm=tk.Menu(m,tearoff=0);fm.add_command(label='Exit',command=root.destroy);m.add_cascade(label='File',menu=fm)
