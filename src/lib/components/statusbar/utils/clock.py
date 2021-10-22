import time

from lib.components.statusbar.utils.button import SButton

class SClock(SButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update()
    
    def update(self):
        time_live = time.strftime("%H:%M:%S")
        self.config(text=time_live) 
        self.after(200, self.update)
