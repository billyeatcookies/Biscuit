import tkinter as tk

from .....components.editor_groups import EditorGroupsPane


class RightTopPane(tk.PanedWindow):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        self.config(orient=tk.HORIZONTAL, bd=0, relief=tk.FLAT)

        self.editor_groups = EditorGroupsPane(self)
        self.editor_groups.configure(height=25)
        self.add(self.editor_groups)
