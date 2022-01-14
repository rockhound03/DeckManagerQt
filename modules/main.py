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
catalog.grid(column=0,row=1,columnspan=2,rowspan=2,sticky=tk.SW)
pageWidth = 700
pageHeight = 280

# Setup tabs
page1 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page2 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page3 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)

catalog.add(page1, text='Set Management')
catalog.add(page2, text='Deck Management')
catalog.add(page3, text='Database Search')
#status_label.pack()
#tk.Label(basePg,text='Classic').pack()
#ttk.Label(basePg,text='Themed').pack()
basePg.mainloop()