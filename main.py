from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


# Creating Functions
def create():
    print("Criando um elemento!")
def update():
    print("Atualizando um elemento!")
def delete():
    print("Deletando um elemento!")
def generate():
    print("Gerando um elemento!")




# Creating Window,variables and elements
root = Tk(className="Gerenciador de Senhas")
root.minsize(825,400)
nameentry = StringVar()
passentry = StringVar()

logo_image = ImageTk.PhotoImage(file = r"images\black_lock_G.png")

# Creating the frame window and frame to the database
window = ttk.Frame(root, borderwidth=5, width=1440, height=1024)

database_image = ttk.Frame(window, borderwidth=10, width=600, height=400,relief='ridge')
registration_frame = ttk.Frame(window,borderwidth=5,width=480, height=400,relief="ridge")
## Image
image_label = ttk.Label(registration_frame, image=logo_image)

## Buttons
create_button = ttk.Button(registration_frame,text="Create", command=create)
generate_button = ttk.Button(registration_frame,text="Generate", command=generate)
update_button = ttk.Button(window,text="Update", command=update)
delete_button = ttk.Button(window,text="Delete", command=delete)

## Input's and Labels
name_label = ttk.Label(registration_frame, text="Site Name: ")
name_input = ttk.Entry(registration_frame, textvariable=nameentry)
pass_label = ttk.Label(registration_frame, text="Site Password: ",)
pass_input = ttk.Entry(registration_frame, textvariable=passentry,show="●")


# Positioning
window.grid(column = 0, row=0,sticky=(N,E,S,W))
registration_frame.grid(column=0, row=0,columnspan=2,rowspan=5,sticky=(N,W,S,E))
database_image.grid(column=3,row=0,columnspan=2,rowspan=5,sticky=(N,E,S,W))

##Buttons
create_button.grid(column=0,row=5,sticky=(W,S))
generate_button.grid(column=1,row=5,sticky=(E,S))

update_button.grid(column=3,row=5, sticky=(E,S))
delete_button.grid(column=4,row=5, sticky=(E,S))

## Entry and Labels
name_label.grid(column=0,row=1, sticky=(W))
name_input.grid(column=0,row=2)
pass_label.grid(column=0,row=3,sticky=(W))
pass_input.grid(column=0,row=4)



# Resizing Configuration
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
#---------------------
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)
#---------------------------
database_image.columnconfigure(0,weight=3)
database_image.rowconfigure(0,weight=1)




if __name__ == "__main__":
    root.mainloop()