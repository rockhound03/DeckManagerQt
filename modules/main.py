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
        
        self.fireBool = tk.BooleanVar()
        self.darkBool = tk.BooleanVar()
        self.electricBool = tk.BooleanVar()
        self.grassBool = tk.BooleanVar()
        self.waterBool = tk.BooleanVar()
        self.psychicBool = tk.BooleanVar()
        self.fightBool = tk.BooleanVar()
        self.metalBool = tk.BooleanVar()

        self.grid(column=0,row=1,columnspan=2,rowspan=2,sticky=tk.SW)
        #options = {'width':550,'height'}
        page1 = ttk.Frame(self,width=550,height=280)
        self.add(page1,text='Set Management')
        page2 = ttk.Frame(self,width=550,height=280)
        self.add(page2,text='Deck Management')
        page3 = ttk.Frame(self,width=550,height=280)
        self.add(page3,text='Database Search')
        page4 = ttk.Frame(self,width=550,height=280)
        self.add(page4,text='Result List')

        self.searchVar = tk.StringVar()

        self.name_search_btn = tk.Button(page3,text='Name Search')
        self.name_search_btn['command'] = self.search_name
        self.name_search_btn['fg'] = "#6DBFE8"
        self.name_search_btn['bg'] = "black"
        self.name_search_btn.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=tk.W)
        
        self.search_text = ttk.Entry(page3,textvariable=self.searchVar)
        self.search_text.grid(column=1,row=1,columnspan=1,rowspan=1,sticky=tk.W,padx=5, pady=5)

    def search_name(self):
        pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Deck Manager - Gen 2')
        self.geometry('700x450+300+40')
        self.resizable(False, False)
        # quit button
        self.quit_button = ttk.Button(self,text='Quit')
        self.quit_button['command'] = lambda: self.quit()
        self.quit_button.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)


if __name__ == "__main__":
    app = App()
    TabFrame(app)
    app.mainloop()
