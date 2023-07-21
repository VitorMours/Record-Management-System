
# About
RMS ( Record Management System ) is a python project that simulates a managing system of some client records in a establishment. The technologies used in this project, are the **sqlite3** and **tkinter**, built-in modules in the python language.

It's an independent project to deepen my knowledge, and the others knowledge that want to contribute to the project. The future of the project have the following planning:

```

First Version
└── [x] - C.R.U.D 
└── [x] - Database view 
Second Version
└── [ ] - Quick Search
└── [ ] - Switch between database tables
Third Version
└── [ ] - Menu Bar 
└── [ ] - Multi Access 
└── [ ] - SQL Search
...

```


# Cloning and Running

## Cloning

### Windows
In the windows environment, the clonning of the repository can be done in the classic way, without bigger problems.

````sh
git clone https://github.com/VitorMours/Record-Management-System.git
````

### Linux
In the linux environment, you can find problems with the fact that python use tkinter, and can not be installed with the python, like what happens in Ubuntu, so you may need to make the adicional instalation of the tkinter, you can do this with:

```sh
# Installing the tkinter package for python
sudo apt-get install python3-tk

git clone https://github.com/VitorMours/Record-Management-System.git
```
## Running
To run the program, you can clone the code, instal python3, and run:
```sh
python3 main.py
```
Or to install as a program, you can clone the code, install python3, install pyinstaller, and run:

```sh
# Installing pyinstaller
pip install -U pyinstaller
# Building the application
pyinstaller main.py
```

# Program Features and Running
The program have the purpose of simulate a commmercial system, so, the features are focused on this, they graphical representation and use are:

<details>
    <summary> Create</summary>
    To create a record inside our RMS, we can use the defined espace to input the data and click on the button "Create". But, to facilitate this, we can also use the Enter button to automatically create the new register, without the necessity to remove the hands of the keyboard
</details>

![](assets/video/Create%20Demonstration.gif)
---

<details>
    <summary>Read</summary>
    By the nature of the project, we can read the database data directly on the interface of the program, by the treeview visualization provided
</details>

---
<details>
    <summary>Update</summary>
    The update command can also be used by the bind <strong> Ctrl+U </strong>. To use this command, you first need to select the record you want to modify, and after this, a window gonna to pop-up, and you can insert the new values in each designed entry, after clicking in the modify, they're going to be updated in the database, and simultaneously in the treeview visualization     
</details>

![](assets/video/Update%20Demonstration.gif)
---

<details>
    <summary>Delete</summary>
    To delete a register from the database, the only need is to select the record, and click in the delete button, or click the <strong>Delete</strong> keyboard 
</details>

![](assets/video/Delete%20Demonstration.gif)







