import sys
import os
import json
import tkinter as tk
from tkinter import ttk
import setmanager
import search_tools
from tkinter.ttk import Label
from config import ROOT_DIR
from PIL import Image, ImageTk
import urllib.request


class TabFrame(ttk.Notebook):
    def __init__(self,container):
        super().__init__(container)
        
        #options = {'width':550,'height'}
        ttk.Frame(self,width=550,height=280).add(0,text='Set Management')
        ttk.Frame(self,width=550,height=280).add(1,text='Deck Management')
        ttk.Frame(self,width=550,height=280).add(2,text='Database Search')
        ttk.Frame(self,width=550,height=280).add(3,text='Result List')


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Deck Manager - Gen 2')
        self.geometry('700x450+300+40')
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    TabFrame(app)
    app.mainloop()
