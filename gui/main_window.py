from tkinter import Tk,Frame
from config.config import APP_NAME,APP_VERSION
from config.constants import *
from gui.header import create as header_create
from gui.toolbar import create as toolbar_create
from gui.sidebar import create as sidebar_create
from gui.statusbar import create as status_create
from gui.url_panel import create as url_create
from gui.video_panel import create as video_create
from gui.download_panel import create as download_create
from gui.progress_panel import create as progress_create
from gui.log_panel import create as log_create

class MainWindow:
    def __init__(self):
        r=self.root=Tk()
        r.title(f'{APP_NAME} {APP_VERSION}')
        r.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        header_create(r).pack(fill='x')
        toolbar_create(r).pack(fill='x')
        body=Frame(r); body.pack(fill='both',expand=True)
        sidebar_create(body).pack(side='left',fill='y')
        content=Frame(body); content.pack(side='left',fill='both',expand=True,padx=8,pady=8)
        url_create(content).pack(fill='x',pady=5)
        video_create(content).pack(fill='x',pady=5)
        download_create(content).pack(fill='x',pady=5)
        progress_create(content).pack(fill='x',pady=5)
        log_create(content).pack(fill='both',expand=True,pady=5)
        status_create(r).pack(side='bottom',fill='x')
    def run(self): self.root.mainloop()

def run():
    MainWindow().run()
