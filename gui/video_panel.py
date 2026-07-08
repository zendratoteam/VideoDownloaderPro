from tkinter import Frame,Label

def create(parent):
 f=Frame(parent,bd=1,relief='groove',padx=10,pady=10)
 t=Frame(f,width=220,height=130,bd=1,relief='sunken');t.pack();t.pack_propagate(False);Label(t,text='Thumbnail').pack(expand=True)
 Label(f,text='Title : -').pack(anchor='w',pady=(10,0));Label(f,text='Uploader : -').pack(anchor='w');Label(f,text='Duration : -').pack(anchor='w');Label(f,text='Resolution : -').pack(anchor='w');return f