import sys
import random
import json
import tkinter as tk
from tkinter import ttk
import setmanager
import search_tools

#https://doc.qt.io/qtforpython/quickstart.html
#https://www.pythontutorial.net/tkinter/

basePg = tk.Tk()
basePg.title('Deck Manager - Gen 1')
basePg.geometry('700x450+300+40')
basePg.grid()
catalog = ttk.Notebook(basePg)
catalog.pack(pady=10,expand=True)
pageWidth = 700
pageHeight = 280

# Setup tabs
page1 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page2 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page3 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)

page1.pack(fill='both', expand=True)
page2.pack(fill='both', expand=True)
page3.pack(fill='both', expand=True)

status_label = ttk.Label(
    page3,
    text='Status: idle',
    padding=3
)

status_label.pack()

def stat_label_callback(status):
    new_string = 'status' + status
    status_label.text = new_string

exit_button = ttk.Button(
    page2,
    text='Quit',
    command=lambda: basePg.quit()
)

checkdb_button = ttk.Button(
    page3,
    text='Check DB',
    command=stat_label_callback('Searching')
)

exit_button.pack(
    ipadx=7,
    ipady=7,
    expand=True
)

checkdb_button.pack(
    ipadx=4,
    ipady=4,
    expand=True
)
catalog.add(page1, text='Sets')
catalog.add(page2, text='Decks')
catalog.add(page3, text='Card Search')
#tk.Label(basePg,text='Classic').pack()
#ttk.Label(basePg,text='Themed').pack()
basePg.mainloop()