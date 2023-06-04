import database

def load_treeview_data(display_element=None):   
    database_data = database.fetch_data()
    for data in database_data:
        display_element.insert("","end",values=(data))
