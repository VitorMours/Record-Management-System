import main
import database
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk





class Update_Window(tk.Tk):
    def __init__(self,user_id,name,surname):
        super().__init__(user_id,name,surname)
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.minsize(330,210)
        self.resizable(False, False)
        self.title("Value Updating Window")
        self.iconbitmap("images\lockicon_120641.ico")
        self.new_name = tk.StringVar()
        self.new_surname = tk.StringVar()

        self.frame = ttk.Frame(self, border=5, borderwidth=20,width=340,height=240)
        self.label_frame = ttk.Labelframe(self.frame,text=" Data Changing ",padding=(10,10,10,10),width=480,height=360)
    
        self.name_label = ttk.Label(self.label_frame, text="New Nome",border=5,borderwidth=10)
        self.name_entry = ttk.Entry(self.label_frame, textvariable=self.new_name)
        self.surname_label = ttk.Label(self.label_frame, text="New Surname",border=5,borderwidth=10)
        self.surname_entry = ttk.Entry(self.label_frame, textvariable=self.new_surname)
        self.div = ttk.Separator(self.label_frame, orient=tk.VERTICAL,)

        self.overview_top = ttk.Separator(self.label_frame, orient=tk.HORIZONTAL)
        self.overview_bottom = ttk.Separator(self.label_frame, orient=tk.HORIZONTAL)

        self.show_old_name = ttk.Label(self.label_frame, text=self.name, foreground="red")
        self.show_new_name = ttk.Label(self.label_frame, textvariable=self.new_name, foreground="green")
        self.show_old_surname = ttk.Label(self.label_frame, text=self.surname, foreground="red")
        self.show_new_surname = ttk.Label(self.label_frame, textvariable=self.new_surname, foreground="green")

        self.modify_button = ttk.Button(self.label_frame, text="Modify", command=lambda:self._update_value())

        self.frame.grid(column=0, row=0,columnspan=5, rowspan=5,sticky=(tk.N,tk.W,tk.E,tk.S))
        self.label_frame.grid(column=0,row=0,columnspan=5,rowspan=5,sticky=(tk.N,tk.W,tk.E,tk.S))
        self.name_label.grid(column=0,row=0,columnspan=2,sticky=(tk.N,tk.W))
        self.name_entry.grid(column=0,row=1,columnspan=2,sticky=(tk.N,tk.W, tk.E))
        self.div.grid(column = 2, row=0, rowspan=2, sticky=(tk.N,tk.S),padx=5)
        self.surname_label.grid(column=3,row=0,columnspan=2,sticky=(tk.N,tk.W))
        self.surname_entry.grid(column=3,row=1,columnspan=2,sticky=(tk.N,tk.W, tk.E))
        
        self.overview_top.grid(column=0,row=2,columnspan=5,sticky=(tk.W,tk.E),pady=5)
        
        self.show_old_name.grid(column=0,row=3,sticky=(tk.W,tk.N))
        self.show_new_name.grid(column=0,row=4)
        
        self.show_old_surname.grid(column=3,row=3,sticky=(tk.W,tk.N))
        self.show_new_surname.grid(column=3,row=4)

        self.overview_bottom.grid(column=0,row=5,columnspan=5, sticky=(tk.W,tk.E),pady=5)

        self.modify_button.grid(column=0,row=6,sticky=(tk.W))

    def create_window(user_id, name,surname):
            update_window = Update_Window(user_id, name,surname)

    def _update_value(self):
        
        database.update_value(self.user_id,self.name_entry.get(),self.surname_entry.get())
        
        super().destroy()


