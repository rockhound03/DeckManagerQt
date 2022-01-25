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

        self.filterBox = ttk.LabelFrame(page3,text='Search Filters')
        self.filterBox.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)
        #fire
        self.fire_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Fire',
                                command=self.filter_ckbox_callback,
                                variable=self.fireBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.fire_ckbox.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)

        # dark
        self.dark_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Dark',
                                command=self.filter_ckbox_callback,
                                variable=self.darkBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.dark_ckbox.grid(column=1,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# fighting
        self.fight_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Fighting',
                                command=self.filter_ckbox_callback,
                                variable=self.fightBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.fight_ckbox.grid(column=2,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# grass
        self.grass_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Grass',
                                command=self.filter_ckbox_callback,
                                variable=self.grassBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.grass_ckbox.grid(column=3,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# electric
        self.electric_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Electric',
                                command=self.filter_ckbox_callback,
                                variable=self.electricBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.electric_ckbox.grid(column=4,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# water
        self.water_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Water',
                                command=self.filter_ckbox_callback,
                                variable=self.waterBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.water_ckbox.grid(column=5,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# psychic
        self.psychic_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Psychic',
                                command=self.filter_ckbox_callback,
                                variable=self.psychicBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.psychic_ckbox.grid(column=6,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# metal
        self.metal_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Metal',
                                command=self.filter_ckbox_callback,
                                variable=self.metalBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.metal_ckbox.grid(column=7,row=0,columnspan=1,rowspan=1,sticky=tk.W)
        column_names =('card_name', 'type', 'set_name','set_series','hp','set_legal')
        self.result_tree = ttk.Treeview(page4, columns=column_names, show='headings')
        self.result_tree.heading('card_name',text='Card Name')
        self.result_tree.heading('type',text='Card Type')
        self.result_tree.heading('set_name',text='Set Name')
        self.result_tree.heading('set_series',text='Set Series')
        self.result_tree.heading('hp',text='Health')
        self.result_tree.heading('set_legal',text='Deck Legal')
        self.result_tree.pack()



    def search_name(self):
        pass

    def filter_ckbox_callback(self):
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
