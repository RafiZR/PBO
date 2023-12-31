import tkinter as tk
from tkinter import Menu
from FrmPersegi import *
from FrmSegitiga import *
from FrmLingkaran import *
from FrmBalok import *
from FrmKerucut import *
from FrmKubus import *
from FrmLimasSegiEmpat import *
from FrmlimasSegiTiga import *
from FrmTabung import *
from FrmPrismaSegiTiga import *

# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Persegi', command= lambda: new_window("Luas Persegi", FrmPersegi)
)
app_menu.add_command(
    label='App Segitiga', command= lambda: new_window("Luas Segitiga", FrmSegitiga)
)
app_menu.add_command(
    label='App Lingkaran', command= lambda: new_window("Luas Lingkaran", FrmLingkaran)

)
app_menu.add_command(
    label='App Balok', command= lambda: new_window("Luas Lingkaran", FrmBalok)

)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Luas Lingkaran", FrmKerucut)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Luas Lingkaran", FrmKubus)
)
app_menu.add_command(
    label='App Limas Segi Empat', command= lambda: new_window("Luas Lingkaran", FrmLimassegiempat)
)
app_menu.add_command(
    label='App Limas Segi Tiga', command= lambda: new_window("Luas Lingkaran", FrmLimasSegiTiga)
)
app_menu.add_command(
    label='App Tabung', command= lambda: new_window("Luas Lingkaran", FrmTabung)
)
app_menu.add_command(
    label='App Prisma Segi Tiga', command= lambda: new_window("Luas Lingkaran", FrmPrismaSegiTiga)

)
#app_menu.add_command(
    #label='App Kerucut', command= lambda: new_window("Luas dan Volume Kerucut", FrmKerucut)


def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
    
root.mainloop()