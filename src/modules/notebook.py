import tkinter as tk 
from tkinter import ttk


class Notebook(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.default = ttk.Frame(self)
        self.add_tab = ttk.Frame(self)

        self.add(self.default, text="<untitled>")
        self.add(self.add_tab, text="+")
        self.bind("<<NotebookTabChanged>>", self._add_tab)
    
    def _add_tab(self, event):
        if self.select() == self.tabs()[-1]:
            index = len(self.tabs()) - 1
       
            table_creation = TableCreationWindow()

            #frame = tk.Frame(self)
            self.insert(index, frame, text="<as>")
            self.select(index)


    def key(self, event):
        print("pressed", repr(event.char))

    def callback(self, event):
        print("clicked at", event.x, event.y, event.type)



        


class TableCreationWindow(tk.Tk):
    def __init__(self):
        super().__init__() 
        self.minsize(330, 210)
        self.resizable(False, False)
        self.title("Creating a new database table")
        self.main_frame = ttk.Frame(self)        
        self.table_info = ttk.Frame(self.main_frame)
        self.table_data = ttk.Frame(self.main_frame)
        self.separator = ttk.Separator(self.main_frame, orient=tk.VERTICAL)
    
        # Configuring elements positions
        self.main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.table_info.grid(column=0, row=0)
        self.separator.grid(column=1, row=0, padx=5)
        self.table_data.grid(column=2, row=0)


