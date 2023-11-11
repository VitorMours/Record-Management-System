import tkinter as tk 

class Menu(tk.Menu):
    def __init__(self, root):
        super().__init__(root)
        # Desativando destacabilidade
        self.option_add("*tearOff", False)
        # Menus
        self.system_menu = tk.Menu(self) 
        self.preferences_menu = tk.Menu(self)
        self.add_cascade(menu=self.system_menu, label="System")
        self.add_cascade(menu=self.preferences_menu, label="Preferences")
        

        # System Menu
        
        self.system_menu.add_command(label=f"New register {'Ctrl+Enter': >15}", command=self.new_register)
        self.system_menu.add_command(label=f"Modify register {'Ctrl+U': >15}", command=self.modify_register)
        self.system_menu.add_command(label=f"Delete register {'Ctrl+del': >15}", command=self.delete_register)

        # Preferences Menu

        self.preferences_menu.add_command(label="Font size", command=self.font)

    def new_register(self):
        print("Novo registro")
    
    def modify_register(self):
        pass

    def delete_register(self):
        pass

    def font(self):
        pass
