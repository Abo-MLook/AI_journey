import sqlite3
from tkinter import *
from tkinter.messagebox import *


# ─────────────────────────────────────────────
# Mosque Class
# ─────────────────────────────────────────────
class Mosque:
    def __init__(self, ID, name, type_, address, coordinates, imam_name):
        self.ID = ID
        self.name = name
        self.type_ = type_
        self.address = address
        self.coordinates = coordinates
        self.imam_name = imam_name


# ─────────────────────────────────────────────
# Database Class
# ─────────────────────────────────────────────
class MosquesDB:
    def __init__(self):
        self.conn = sqlite3.connect('Mosques.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Mosq (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Type TEXT,
            Address TEXT,
            Coordinates TEXT,
            Imam_name TEXT
        )''')
        self.conn.commit()

    def Display(self):
        self.cur.execute("SELECT * FROM Mosq")
        return self.cur.fetchall()

    def Search(self, name):
        self.cur.execute("SELECT * FROM Mosq WHERE Name=?", (name,))
        return self.cur.fetchone()

    def Insert(self, ID, name, type_, address, coordinates, imam_name):
        self.cur.execute(
            "INSERT INTO Mosq VALUES (?,?,?,?,?,?)",
            (ID, name, type_, address, coordinates, imam_name)
        )
        self.conn.commit()

    def Delete(self, ID):
        self.cur.execute("DELETE FROM Mosq WHERE ID=?", (ID,))
        self.conn.commit()

    def Update(self, name, imam_name):
        self.cur.execute(
            "UPDATE Mosq SET Imam_name=? WHERE Name=?",
            (imam_name, name)
        )
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# ─────────────────────────────────────────────
# GUI Application
# ─────────────────────────────────────────────
db = MosquesDB()

top = Tk()
top.title("Mosques Management System")
top.geometry("700x420")
top.resizable(False, False)

# ── Part 1: Input Fields ──────────────────────
Label(top, text="ID").grid(row=0, column=0, padx=8, pady=6, sticky=W)
e_id = Entry(top, width=18)
e_id.grid(row=0, column=1, padx=4, pady=6)

Label(top, text="Name").grid(row=0, column=2, padx=8, sticky=W)
e_name = Entry(top, width=18)
e_name.grid(row=0, column=3, padx=4)

Label(top, text="Type").grid(row=1, column=0, padx=8, pady=6, sticky=W)
type_var = StringVar(top)
type_var.set("Jami")
option_type = OptionMenu(top, type_var, "Jami", "Neighborhood", "Friday")
option_type.config(width=14)
option_type.grid(row=1, column=1, padx=4)

Label(top, text="Address").grid(row=1, column=2, padx=8, sticky=W)
e_address = Entry(top, width=18)
e_address.grid(row=1, column=3, padx=4)

Label(top, text="Coordinates").grid(row=2, column=0, padx=8, pady=6, sticky=W)
e_coords = Entry(top, width=18)
e_coords.grid(row=2, column=1, padx=4)

Label(top, text="Imam_name").grid(row=2, column=2, padx=8, sticky=W)
e_imam = Entry(top, width=18)
e_imam.grid(row=2, column=3, padx=4)

# ── Part 2: ListBox ───────────────────────────
listbox = Listbox(top, width=55, height=12)
listbox.grid(row=0, column=4, rowspan=6, padx=10, pady=6, sticky=N)

scrollbar = Scrollbar(top)
scrollbar.grid(row=0, column=5, rowspan=6, sticky=NS)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# ── Helper: clear input fields ────────────────
def clear_fields():
    e_id.delete(0, END)
    e_name.delete(0, END)
    e_address.delete(0, END)
    e_coords.delete(0, END)
    e_imam.delete(0, END)
    type_var.set("Jami")

# ── Button Callbacks ──────────────────────────
def display_all():
    listbox.delete(0, END)
    records = db.Display()
    if not records:
        listbox.insert(END, "No records found.")
        return
    listbox.insert(END, f"{'ID':<10} {'Name':<20} {'Type':<14} {'Address':<18} {'Coords':<16} {'Imam'}")
    listbox.insert(END, "-" * 90)
    for row in records:
        listbox.insert(END, f"{str(row[0]):<10} {str(row[1]):<20} {str(row[2]):<14} {str(row[3]):<18} {str(row[4]):<16} {row[5]}")

def search_by_name():
    name = e_name.get().strip()
    if not name:
        showwarning("Input Error", "Please enter a mosque name to search.")
        return
    listbox.delete(0, END)
    record = db.Search(name)
    if record:
        listbox.insert(END, f"{'ID':<10} {'Name':<20} {'Type':<14} {'Address':<18} {'Coords':<16} {'Imam'}")
        listbox.insert(END, "-" * 90)
        listbox.insert(END, f"{str(record[0]):<10} {str(record[1]):<20} {str(record[2]):<14} {str(record[3]):<18} {str(record[4]):<16} {record[5]}")
    else:
        listbox.insert(END, f"No mosque found with name: {name}")

def add_entry():
    id_val   = e_id.get().strip()
    name     = e_name.get().strip()
    type_    = type_var.get()
    address  = e_address.get().strip()
    coords   = e_coords.get().strip()
    imam     = e_imam.get().strip()

    if not id_val or not name:
        showwarning("Input Error", "ID and Name are required.")
        return
    try:
        mosque = Mosque(int(id_val), name, type_, address, coords, imam)
        db.Insert(mosque.ID, mosque.name, mosque.type_, mosque.address,
                  mosque.coordinates, mosque.imam_name)
        showinfo("Success", f"Mosque '{name}' added successfully.")
        clear_fields()
        display_all()
    except Exception as e:
        showerror("Error", str(e))

def delete_entry():
    id_val = e_id.get().strip()
    if not id_val:
        showwarning("Input Error", "Please enter the mosque ID to delete.")
        return
    if askyesno("Confirm Delete", f"Delete mosque with ID {id_val}?"):
        db.Delete(int(id_val))
        showinfo("Deleted", f"Mosque ID {id_val} deleted.")
        clear_fields()
        display_all()

def update_entry():
    name  = e_name.get().strip()
    imam  = e_imam.get().strip()
    if not name or not imam:
        showwarning("Input Error", "Please enter mosque Name and new Imam_name.")
        return
    db.Update(name, imam)
    showinfo("Updated", f"Imam name updated for '{name}'.")
    display_all()

# ── Part 3: Operation Buttons ─────────────────
btn_frame = Frame(top)
btn_frame.grid(row=3, column=0, columnspan=4, pady=10)

Button(btn_frame, text="Display All",    width=13, command=display_all).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Search By Name", width=13, command=search_by_name).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Update Entry",   width=13, command=update_entry).grid(row=0, column=2, padx=5)

Button(btn_frame, text="Add Entry",   width=13, command=add_entry).grid(row=1, column=0, padx=5, pady=4)
Button(btn_frame, text="Delete Entry", width=13, command=delete_entry).grid(row=1, column=1, padx=5)
Button(btn_frame, text="Clear Fields", width=13, command=clear_fields).grid(row=1, column=2, padx=5)

top.mainloop()
