from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database
import functions

def create():
    nome = name_input.get()
    sobrenome = last_input.get()

    if nome.strip() == "" or sobrenome.strip() == "":
        messagebox.showerror("Gerenciador de Cadastros - Erro de usuário", "A senha ou site não pode ter um valor vazio passado")
    
    row_id = database.fetch_last_id() 
    database.insert(nome,sobrenome)
    treeview.insert("", "end", values=(row_id+1,nome,sobrenome))
    last_input.delete(0,END)
    name_input.delete(0,END)

def update():
    print("Atualizando um elemento!")
def delete():
    print("Deletando um elemento!")
def read():
    print("Gerando um elemento!")





# Creating Window,variables and elements
root = Tk(className=" Gerenciador de Cadastros v1.0.0")
root.minsize(825,400)
nameentry = StringVar()
last_nameentry = StringVar()
root.iconbitmap("images\lockicon_120641.ico")

# Creating the frame window and frame to the database
window = ttk.Frame(root, borderwidth=5, width=1440, height=1024)
database_image = ttk.Frame(window, borderwidth=10, width=600, height=400,relief='sunken')
registration_frame = ttk.Frame(window,borderwidth=5,width=480, height=400,relief="sunken")

# Treeview to see the database
treeview = ttk.Treeview(database_image, columns=("index","Name","Surname"),show="headings")
treeview.heading("index",text="ID")
treeview.heading("Name",text="Name")
treeview.heading("Surname",text="Surname")
# --------------------------------------------
treeview.column("index", width=40, stretch=NO)
# Treeview Scroll
scroll = ttk.Scrollbar(database_image, orient="vertical", command=treeview.yview)
scroll.grid(column=6, row=0,rowspan=5,sticky=(N,S))


## Buttons
create_button = ttk.Button(registration_frame,text="Create", command=lambda:create())
read_button = ttk.Button(registration_frame,text="Read", command=lambda:read())
update_button = ttk.Button(window,text="Update", command=lambda:update())
delete_button = ttk.Button(window,text="Delete", command=lambda:delete())

## Input's and Labels
name_label = ttk.Label(registration_frame, text="Name: ")
name_input = ttk.Entry(registration_frame, textvariable=nameentry)
last_label = ttk.Label(registration_frame, text="Surname: ",)
last_input = ttk.Entry(registration_frame, textvariable=last_nameentry)

# SQL search



# Positioning
window.grid(column = 0, row=0,sticky=(N,E,S,W))
registration_frame.grid(column=0, row=0,columnspan=2,rowspan=5,sticky=(N,W,S,E))
database_image.grid(column=3,row=0,columnspan=3,rowspan=5,sticky=(N,E,S,W))

##Buttons
create_button.grid(column=0,row=5,sticky=(W,S))
read_button.grid(column=1,row=5,sticky=(E,S))
update_button.grid(column=3,row=5, sticky=(W,S))
delete_button.grid(column=4,row=5, sticky=(E,S))

## Entry and Labels
name_label.grid(column=0,row=1, sticky=(W))
name_input.grid(column=0,row=2, sticky=(W,E), columnspan=2)
last_label.grid(column=0,row=3,sticky=(W))
last_input.grid(column=0,row=4, sticky=(W,E), columnspan=2)



#Treeview
treeview.grid(column=0,row=0,sticky=(N,W,E,S))
treeview.configure(yscrollcommand=scroll.set)

# Resizing Configuration
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
#----------------------------------
window.columnconfigure(0,weight=0)
window.rowconfigure(0,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)
#----------------------------------
database_image.columnconfigure(0,weight=3)
database_image.rowconfigure(0,weight=1)
treeview.columnconfigure(0, weight=3)
treeview.rowconfigure(0, weight=1)




if __name__ == "__main__":
    database.create("informacao_clientes")
    
    functions.load_treeview_data(treeview)
    
    root.mainloop()