import sys
import random
import json
import tkinter as tk
from tkinter import ttk

#https://doc.qt.io/qtforpython/quickstart.html
#https://www.pythontutorial.net/tkinter/

basePg = tk.Tk()
basePg.title('Deck Manager - Gen 1')
basePg.geometry('700x450+300+40')
catalog = ttk.Notebook(basePg)
catalog.pack(pady=10,expand=True)
pageWidth = 700
pageHeight = 280

page1 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page2 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page3 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)

page1.pack(fill='both', expand=True)
page2.pack(fill='both', expand=True)
page3.pack(fill='both', expand=True)

exit_button = ttk.Button(
    page2,
    text='Quit',
    command=lambda: basePg.quit()
)

exit_button.pack(
    ipadx=7,
    ipady=7,
    expand=True
)
catalog.add(page1, text='Sets')
catalog.add(page2, text='Decks')
catalog.add(page3, text='Card Search')
#tk.Label(basePg,text='Classic').pack()
#ttk.Label(basePg,text='Themed').pack()
basePg.mainloop()