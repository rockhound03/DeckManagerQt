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
        self.page1 = ttk.Frame(self,width=550,height=280)
        self.add(self.page1,text='Set Management')
        self.page2 = ttk.Frame(self,width=550,height=280)
        self.add(self.page2,text='Deck Management')
        self.page3 = ttk.Frame(self,width=550,height=280)
        self.add(self.page3,text='Database Search')
        self.page4 = ttk.Frame(self,width=550,height=280)
        self.add(self.page4,text='Result List')

        self.searchVar = tk.StringVar()

        self.name_search_btn = tk.Button(self.page3,text='Name Search')
        self.name_search_btn['command'] = self.search_name
        self.name_search_btn['fg'] = "#6DBFE8"
        self.name_search_btn['bg'] = "black"
        self.name_search_btn.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=tk.W)

        
        self.search_text = ttk.Entry(self.page3,textvariable=self.searchVar)
        self.search_text.grid(column=1,row=1,columnspan=1,rowspan=1,sticky=tk.W,padx=5, pady=5)

        self.clear_report_btn = tk.Button(self.page3,text='Clear Search')
        self.clear_report_btn['command'] = self.clear_tree
        self.clear_report_btn['fg'] = "#6DBFE8"
        self.clear_report_btn['bg'] = "black"
        self.clear_report_btn.grid(column=2,row=1,columnspan=1,rowspan=1,sticky=tk.W)

        self.filterBox = ttk.LabelFrame(self.page3,text='Search Filters')
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
        self.result_tree = ttk.Treeview(self.page4, columns=column_names, show='headings')
        self.result_tree.heading('card_name',text='Card Name')
        self.result_tree.heading('type',text='Card Type')
        self.result_tree.heading('set_name',text='Set Name')
        self.result_tree.heading('set_series',text='Set Series')
        self.result_tree.heading('hp',text='Health')
        self.result_tree.heading('set_legal',text='Deck Legal')
        self.result_tree.pack()



    def search_name(self):
        with open(os.path.join(ROOT_DIR,'data','cards.json'),"r") as cards_file:
            cards_obj = json.load(cards_file)
        cards = cards_obj['data']

        search_item = self.search_text.get()
        #result_list.clear()
        result_data = search_tools.name_search(cards, search_item)
        card_results = []
        for result in result_data:
            card_results.append((result['name'],result['supertype'],result['setName'],result['setSeries'],result['hp'],result['setLegal']))

        for card_result in card_results:
            self.result_tree.insert('', tk.END, values=card_result)
        self.result_tree.pack()
        print(str(self.result_tree.winfo_children()))


    def filter_ckbox_callback(self):
        pass

    def clear_tree(self):
        counter = 0
        for obwidget in self.page4.winfo_children():
            counter += 1
        print(str(counter))

    def setup_tree(self):
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
