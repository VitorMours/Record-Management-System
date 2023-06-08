import database
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def load_treeview_data(display_element=None):   
    database_data = database.fetch_data()
    for data in database_data:
        display_element.insert("","end",values=(data))





class Update_Window(tk.Tk):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.name = name
        self.surname = surname
        self.minsize(480,360)
        self.maxsize(480,360)
        self.resizable(False,False)
        self.title("Value Updating Window")
        self.iconbitmap("images\lockicon_120641.ico")
        new_name = tk.StringVar()
        new_surname = tk.StringVar()

        self.frame = ttk.Frame(self, border=5, borderwidth=20,width=480,height=360)
        self.label_frame = ttk.Labelframe(self.frame,text=" Data Changing ",padding=(10,10,10,10),width=480,height=360)
    
        self.name_label = ttk.Label(self.label_frame, text="New Nome",border=5,borderwidth=10)
        self.name_entry = ttk.Entry(self.label_frame, textvariable=new_name)
        self.surname_label = ttk.Label(self.label_frame, text="New Surname",border=5,borderwidth=10)
        self.surname_entry = ttk.Entry(self.label_frame, textvariable=new_surname)
        self.div = ttk.Separator(self.label_frame, orient=tk.VERTICAL,)

        self.overview = ttk.Separator(self.label_frame, orient=tk.HORIZONTAL)


        self.show_old_name = ttk.Label(self.label_frame, text=self.name, foreground="red")
        self.show_new_name = ttk.Label(self.label_frame, textvariable=new_name, foreground="green")
        self.show_old_surname = ttk.Label(self.label_frame, text=self.surname, foreground="red")
        self.show_new_surname = ttk.Label(self.label_frame, textvariable=new_surname, foreground="green")


        self.frame.grid(column=0, row=0,columnspan=5, rowspan=5,sticky=(tk.N,tk.W,tk.E,tk.S))
        self.label_frame.grid(column=0,row=0,columnspan=5,rowspan=5,sticky=(tk.N,tk.W,tk.E,tk.S))
        self.name_label.grid(column=0,row=0,columnspan=2,sticky=(tk.N,tk.W))
        self.name_entry.grid(column=0,row=1,columnspan=2,sticky=(tk.N,tk.W))
        self.div.grid(column = 2, row=0, rowspan=2, sticky=(tk.N,tk.S),padx=5)
        self.surname_label.grid(column=3,row=0,columnspan=2,sticky=(tk.N,tk.W))
        self.surname_entry.grid(column=3,row=1,columnspan=2,sticky=(tk.N,tk.W))
        self.overview.grid(column=0,row=2,columnspan=5,sticky=(tk.W,tk.E),pady=5)
        
        self.show_old_name.grid(column=0,row=3,sticky=(tk.W,tk.N))
        self.show_new_name.grid(column=0,row=4)
        
        self.show_old_surname.grid(column=3,row=3,sticky=(tk.W,tk.N))
        self.show_new_surname.grid(column=3,row=4)




    def crete_window(name,surname):
            update_window = Update_Window(name,surname)



