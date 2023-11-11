import tkinter as tk
#from PIL import Image, ImageTk
from tkinter import ttk, font
from tkinter import messagebox

from modules import menu, notebook
import database
import functions





class App(tk.Tk):

    def __init__(self, title:str = "Information Manager v1.0"):
        super().__init__()
        self.modified_list = []
        # Window Atributes
#        self.image = Image.open(r"images\lockicon_120641.ico")
#        self.icon = ImageTk.PhotoImage(self.image)
#        self.iconphoto(True,self.icon)
#        self.iconbitmap("images\lockicon_120641.ico")
        self.title(title)
        self.minsize(825,400)
        self.menubar = menu.Menu(self)
        self['menu'] = self.menubar
        #Font
        self.DefaultFont = font.nametofont("TkDefaultFont")
        self.TextFont = font.Font(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.DefaultFont.configure(family="@Microsoft JhengHei UI", weight=font.BOLD)

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
        self.delete_button = ttk.Button(self.main_frame,text="Delete", command=lambda:self._delete())

        # Normal and Scrolling Treeview Settings
        self.notebook = notebook.Notebook(self.database_image)
        
        # TODO Get this scroll script and do inside the notebook
        # Treeview Scroll
        #self.scroll = ttk.Scrollbar(self.database_image, orient="vertical", command=self.treeview.yview)

        # Griding Elements
        ## Frames and Big Elements
        self.main_frame.grid(column = 0, row=0,sticky=(tk.N,tk.E,tk.S,tk.W))
        self.registration_frame.grid(column=0, row=0,columnspan=2,rowspan=5,sticky=(tk.N,tk.W,tk.S,tk.E))
        self.database_image.grid(column=3,row=0,columnspan=3,rowspan=5,sticky=(tk.N,tk.E,tk.S,tk.W))
        self.notebook.grid(column=0,row=0,sticky=(tk.N,tk.W,tk.E,tk.S))

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
        self.notebook.columnconfigure(0, weight=3)
        self.notebook.rowconfigure(0, weight=1)
        #self.treeview.configure(yscrollcommand=self.scroll.set)

        # Widget Binds
        
    def aply_color(self):
        for idx, item in enumerate(self.treeview.get_children()):
            if idx % 2 == 0:
                self.treeview.item(item, tags=('pair',))
            else:
                self.treeview.item(item, tags=('odd',))
        self.treeview.tag_configure("pair", background="#FFFFFF")
        self.treeview.tag_configure("odd", background="#F0F0F0")


    def _create(self, event=None):
        nome = self.name_input.get()
        sobrenome = self.surname_input.get()
        if nome.strip() == "" or sobrenome.strip() == "":
            messagebox.showerror("Information Manager - Creation Error", "The name or surname cannot be a empty or whitespace only value")
        else:
            database.insert(nome,sobrenome)
            row_id = database.fetch_last_id() 
            self.treeview.insert("", "end", values=(row_id+1,nome,sobrenome))
            self.name_input.delete(0,tk.END)
            self.surname_input.delete(0,tk.END)
            self.aply_color()

    def _update(self, event=None):
        selected = self.treeview.focus()
        temp = self.treeview.item(selected, "values")
        try:
            window = functions.Update_Window(temp[0],temp[1],temp[2])
            self.main_window_function(False)
            window.wait_window()
            self.main_window_function(True)

        except(IndexError):
            messagebox.showerror("Information Manager - Data Error","You need to select the data you want to modify in the treeview vision")
        
        finally:
            self.treeview.delete(*self.treeview.get_children())
            self._load_treeview_data()

    def _delete(self, event=None):
        try :
            values = self.treeview.item(self.treeview.focus(), "values")
            database.delete_value(values[0],values[1])
            self.treeview.delete(self.treeview.selection())
        except (IndexError):
            messagebox.showerror("Information Manager - Selection Error", "You need to select the data you want to delete from the database")
        self.aply_color()   

  




    def main_window_function(self, status):
        if status:
            #Biding
            self.create_button.bind("<Return>",self._create)
            self.name_input.bind("<Return>",self._create)
            self.surname_input.bind("<Return>",self._create)
            self.bind("<Delete>", self._delete)
            self.bind("<Control-u>", self._update)

            #Buttons
            self.update_button.config(state="normal")
            self.create_button.config(state="normal")
            self.delete_button.config(state="normal")
            self.name_input.config(state="normal")
            self.surname_input.config(state="normal")

        else:
            #Bidings
            self.unbind("<Control-u>")
            self.create_button.unbind("<Return>")
            self.name_input.unbind("<Return>")
            self.surname_input.unbind("<Return>")
            self.unbind("<Delete>")

            #Buttons
            self.update_button.config(state="disable")
            self.create_button.config(state="disable")
            self.delete_button.config(state="disable")
            self.name_input.config(state="disable")
            self.surname_input.config(state="disable")

    def _add_menubar(self):
        pass




if __name__ == "__main__":
    database.create("informacao_clientes")

    app = App("Information Manager v1.0")
    app.main_window_function(True)
    app.mainloop()
