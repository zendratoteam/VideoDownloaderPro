from tkinter import Frame,Label,Button
from tkinter.ttk import Combobox

def create(parent):
 f=Frame(parent,bd=1,relief='groove',padx=10,pady=10);Label(f,text='Video Format').pack(anchor='w');Combobox(f,values=['MP4 1080p','MP4 720p','MP3 320kbps','Best Available']).pack(fill='x',pady=5);Button(f,text='Download Now').pack(anchor='e',pady=8);return f