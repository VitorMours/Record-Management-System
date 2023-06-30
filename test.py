import tkinter as tk
from tkinter import ttk

def atualizar_elemento():
    selected_item = treeview.selection()

    if selected_item:
        # Obter novos valores (exemplo)
        novos_valores = ("Novo Nome", "Nova Idade")

        # Atualizar os valores do item selecionado
        treeview.item(selected_item, text=novos_valores[0], values=(novos_valores[1]))

root = tk.Tk()

treeview = ttk.Treeview(root)
treeview.pack()

treeview["columns"] = ("Idade")
treeview.heading("#0", text="Nome")
treeview.heading("Idade", text="Idade")

treeview.insert("", "end", text="João", values=("25"))
treeview.insert("", "end", text="Maria", values=("30"))
treeview.insert("", "end", text="Pedro", values=("35"))

button_atualizar = tk.Button(root, text="Atualizar Elemento", command=atualizar_elemento)
button_atualizar.pack()

root.mainloop()