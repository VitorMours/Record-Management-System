import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import database
import functions


def delete():
    print("Deletando um elemento!")



class App(tk.Tk):
    def __init__(self, title:str):
        super().__init__()
        # Window Atributes
        self.iconbitmap("images\lockicon_120641.ico")
        self.title(title)
        self.minsize(825,400)

        #Frames
        self.main_frame = ttk.Frame(self, borderwidth=5, width=825, height=400)
        self.database_image = ttk.Frame(self.main_frame, borderwidth=10, width=600, height=400)
        self.registration_frame = ttk.Frame(self.main_frame,borderwidth=5,width=250, height=400)
        

        # Input Widgets and Elements
        self.name_entry = tk.StringVar()
        self.surname_entry = tk.StringVar()
        self.name_label = ttk.Label(self.registration_frame, text="Name: ")
        self.surname_label = ttk.Label(self.registration_frame, text="Surname: ",)
        self.name_input = ttk.Entry(self.registration_frame, textvariable=self.name_entry,cursor="xterm")
        self.surname_input = ttk.Entry(self.registration_frame, textvariable=self.surname_entry,cursor="xterm")


        # Buttons
        self.create_button = ttk.Button(self.registration_frame,text="Create", command=lambda:self._create())
        self.update_button = ttk.Button(self.main_frame,text="Update", command=lambda:self._update())
        self.delete_button = ttk.Button(self.main_frame,text="Delete", command=lambda:delete())


        # Normal and Scrolling Treeview Settings
        self.treeview = ttk.Treeview(self.database_image, columns=("index","Name","Surname"),show="headings")
        self.treeview.heading("index",text="ID")
        self.treeview.heading("Name",text="Name")
        self.treeview.heading("Surname",text="Surname")
        self.treeview.column("index", width=40, stretch=tk.NO)


        # Treeview Scroll
        self.scroll = ttk.Scrollbar(self.database_image, orient="vertical", command=self.treeview.yview)


        # Griding Elements
        ## Frames and Big Elements
        self.main_frame.grid(column = 0, row=0,sticky=(tk.N,tk.E,tk.S,tk.W))
        self.registration_frame.grid(column=0, row=0,columnspan=2,rowspan=5,sticky=(tk.N,tk.W,tk.S,tk.E))
        self.database_image.grid(column=3,row=0,columnspan=3,rowspan=5,sticky=(tk.N,tk.E,tk.S,tk.W))
        self.treeview.grid(column=0,row=0,sticky=(tk.N,tk.W,tk.E,tk.S))
        self.treeview.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(column=6, row=0,rowspan=6,sticky=(tk.N,tk.S))

        ## Labels and Entries
        self.name_label.grid(column=0,row=1, sticky=(tk.W))
        self.surname_label.grid(column=0,row=3,sticky=(tk.W))
        self.name_input.grid(column=0,row=2, sticky=(tk.W,tk.E), columnspan=2)
        self.surname_input.grid(column=0,row=4, sticky=(tk.W,tk.E), columnspan=2)

        ##Buttons
        self.create_button.grid(column=0,row=5,sticky=(tk.W,tk.S),pady=5)
        self.update_button.grid(column=3,row=5, sticky=(tk.W,tk.S), padx=9)
        self.delete_button.grid(column=4,row=5, sticky=(tk.E,tk.S), padx=25)

        ## Resizing and others Configuration
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        #--------------------------------------------------
        self.main_frame.columnconfigure(0,weight=0)
        self.main_frame.rowconfigure(0,weight=1)
        self.main_frame.columnconfigure(3,weight=1)
        self.main_frame.columnconfigure(4,weight=1)
        #--------------------------------------------------
        self.database_image.columnconfigure(0,weight=3)
        self.database_image.rowconfigure(0,weight=1)
        self.treeview.columnconfigure(0, weight=3)
        self.treeview.rowconfigure(0, weight=1)
        self.treeview.configure(yscrollcommand=self.scroll.set)

    def load_treeview_data(self):   
        database_data = database.fetch_data()
        for data in database_data:
            self.treeview.insert("","end",values=(data))
 
    def _create(self):
        nome = self.name_input.get()
        sobrenome = self.surname_input.get()

        if nome.strip() == "" or sobrenome.strip() == "":
            messagebox.showerror("Gerenciador de Cadastros - Erro de usuário", "A senha ou site não pode ter um valor vazio passado")
        database.insert(nome,sobrenome)
        row_id = database.fetch_last_id() 
        self.treeview.insert("", "end", values=(row_id+1,nome,sobrenome))
        self.name_input.delete(0,tk.END)
        self.surname_input.delete(0,tk.END)

    def _update(self):
        selected = self.treeview.focus()
        temp = self.treeview.item(selected, "values")
        try:
            functions.Update_Window.create_window(str(temp[0]),str(temp[1]),str(temp[2]))
            self.load_treeview_data()

        except(IndexError):
            messagebox.showerror("Data Error","You need to select the data you want to modify in the treeview vision")



if __name__ == "__main__":
    database.create("informacao_clientes")
    
    
    app = App("Information Manager")
    app.load_treeview_data()

    app.mainloop()