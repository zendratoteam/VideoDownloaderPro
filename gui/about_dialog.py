from tkinter import messagebox
from config.config import APP_NAME,APP_VERSION

def show(): messagebox.showinfo('About',f'{APP_NAME} {APP_VERSION}')
