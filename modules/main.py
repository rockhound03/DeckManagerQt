import sys
import os
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
import setmanager
import search_tools
import gui_init
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
        self.fairyBool = tk.BooleanVar()
        self.dragonBool = tk.BooleanVar()

        self.expandBool = tk.BooleanVar()
        self.unlimitBool = tk.BooleanVar()
        self.standardBool = tk.BooleanVar()

        self.hpEqual = tk.StringVar()
        self.hpSearchVar = tk.StringVar()
        self.filterTerms = gui_init.filter_bool_init()
        self.cardSetNames = gui_init.load_set_names()
        self.searchSetName = tk.StringVar()
        self.searchVar = tk.StringVar()
        self.abilityVar = tk.StringVar()

        self.grid(column=0,row=1,columnspan=2,rowspan=2,sticky=tk.SW)
        #options = {'width':550,'height'}
        self.page1 = ttk.Frame(self,width=750,height=380)
        self.add(self.page1,text='Set Management')
        self.page2 = ttk.Frame(self,width=750,height=380)
        self.add(self.page2,text='Deck Management')
        self.page3 = ttk.Frame(self,width=750,height=380)
        self.add(self.page3,text='Database Search')
        self.page4 = ttk.Frame(self,width=750,height=380)
        self.add(self.page4,text='Result List')

        

        # Filter box setups: 
        self.filterBox = ttk.LabelFrame(self.page3,text='Search Filters: Energy Type')
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
        # fairy
        self.fairy_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Fairy',
                                command=self.filter_ckbox_callback,
                                variable=self.fairyBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.fairy_ckbox.grid(column=8,row=0,columnspan=1,rowspan=1,sticky=tk.W)
        # dragon
        self.dragon_ckbox = ttk.Checkbutton(self.filterBox,
                                text='Dragon',
                                command=self.filter_ckbox_callback,
                                variable=self.dragonBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.dragon_ckbox.grid(column=9,row=0,columnspan=1,rowspan=1,sticky=tk.W)

        self.legalBox = ttk.LabelFrame(self.page3,text='Search Filters: Tournament Legal')
        self.legalBox.grid(column=0,row=1,padx=5,pady=5,sticky=tk.W)
        # expanded
        self.expand_ckbox = ttk.Checkbutton(self.legalBox,
                                text='Expanded',
                                command=self.filter_ckbox_callback,
                                variable=self.expandBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.expand_ckbox.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)
        # unlimited
        self.unlimit_ckbox = ttk.Checkbutton(self.legalBox,
                                text='Unlimited',
                                command=self.filter_ckbox_callback,
                                variable=self.unlimitBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.unlimit_ckbox.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=tk.W)
        # standard
        self.standard_ckbox = ttk.Checkbutton(self.legalBox,
                                text='Standard',
                                command=self.filter_ckbox_callback,
                                variable=self.standardBool,
                                onvalue=True,
                                offvalue=False
                                )
        self.standard_ckbox.grid(column=0,row=2,columnspan=1,rowspan=1,sticky=tk.W)

        self.HPfilterbox = ttk.LabelFrame(self.page3,text='Search Filters: HP Points')
        self.HPfilterbox.grid(column=2,row=1,padx=5,pady=5,sticky=tk.E)
        self.hpradio1 = ttk.Radiobutton(self.HPfilterbox, text='Greater than', value='GT',variable=self.hpEqual)
        self.hpradio1.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)
        self.hpradio2 = ttk.Radiobutton(self.HPfilterbox, text='Less than', value='LT',variable=self.hpEqual)
        self.hpradio2.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=tk.W)
        self.hpradio3 = ttk.Radiobutton(self.HPfilterbox, text='Equal to', value='EQ',variable=self.hpEqual)
        self.hpradio3.grid(column=0,row=2,columnspan=1,rowspan=1,sticky=tk.W)
        self.hp_search = ttk.Entry(self.HPfilterbox,textvariable=self.hpSearchVar)
        self.hp_search.grid(column=0,row=3,columnspan=1,rowspan=1,sticky=tk.W)

        self.setListDropdown = ttk.OptionMenu(
            self.page3,
            self.searchSetName,
            self.cardSetNames[0],
            *self.cardSetNames,
            command=self.select_setname
        )
        self.setListDropdown.grid(column=1,row=1,padx=5,pady=5,sticky=tk.W)

        self.nameSearchBox = ttk.LabelFrame(self.page3,text='Search: Card Name')
        self.nameSearchBox.grid(column=0,row=3,padx=5,pady=5,sticky=tk.W)
        self.search_text = ttk.Entry(self.nameSearchBox,textvariable=self.searchVar)
        self.search_text.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W,padx=2, pady=2)
        self.name_search_btn = tk.Button(self.nameSearchBox,text='Name Search')
        self.name_search_btn['command'] = self.search_name
        self.name_search_btn['fg'] = "#6DBFE8"
        self.name_search_btn['bg'] = "black"
        self.name_search_btn.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=tk.W)
        self.clear_report_btn = tk.Button(self.nameSearchBox,text='Clear Search')
        self.clear_report_btn['command'] = self.clear_tree
        self.clear_report_btn['fg'] = "#6DBFE8"
        self.clear_report_btn['bg'] = "black"
        self.clear_report_btn.grid(column=0,row=2,columnspan=1,rowspan=1,sticky=tk.W)

        self.abilitySearchBox = ttk.LabelFrame(self.page3,text='Search: Ability name')
        self.abilitySearchBox.grid(column=1,row=3,padx=5,pady=5,sticky=tk.W)
        self.ability_search_text = ttk.Entry(self.abilitySearchBox,textvariable=self.abilityVar)
        self.ability_search_text.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W,padx=5, pady=5)
        self.ability_search_btn = tk.Button(self.abilitySearchBox,text='Ability Search')
        self.ability_search_btn['command'] = self.search_name
        self.ability_search_btn['fg'] = "#6DBFE8"
        self.ability_search_btn['bg'] = "black"
        self.ability_search_btn.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=tk.W)

        self.advancedSearchBox = ttk.LabelFrame(self.page3,text='Search: Advanced')
        self.advancedSearchBox.grid(column=1,row=4,padx=5,pady=5,sticky=tk.W)
        self.advance_search_btn = tk.Button(self.advancedSearchBox,text='Advanced Search')
        self.advance_search_btn['command'] = self.advanced_search
        self.advance_search_btn['fg'] = "#6DBFE8"
        self.advance_search_btn['bg'] = "black"
        self.advance_search_btn.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=tk.W)

        self.setup_tree()


    def search_name(self):
        cards = search_tools.load_card_data()
        search_item = self.search_text.get()
        
        result_data = search_tools.name_search(cards, search_item)
        card_results = []
        for result in result_data:
            card_results.append((result['name'],result['supertype'],result['setName'],result['setSeries'],result['hp'],result['setLegal']))

        for card_result in card_results:
            self.result_tree.insert('', tk.END, values=card_result)
        self.result_tree.pack()
        print(str(self.result_tree.winfo_children()))

    def search_ability_name(self):
        cards = search_tools.load_card_data()
        search_item = self.ability_search_text.get()
        result_data = search_tools.search_ability_names(cards, search_item)
        card_results = []
        for result in result_data:
            card_results.append((result['name'],result['supertype'],result['setName'],result['setSeries'],result['hp'],result['setLegal']))

        for card_result in card_results:
            self.result_tree.insert('', tk.END, values=card_result)
        self.result_tree.pack()
        print(str(self.result_tree.winfo_children()))

    def filter_ckbox_callback(self):
        self.filterTerms['energy_filter']['fire'] = self.fireBool.get()
        self.filterTerms['energy_filter']['dark'] = self.darkBool.get()
        self.filterTerms['energy_filter']['fighting'] = self.fightBool.get()
        self.filterTerms['energy_filter']['grass'] = self.grassBool.get()
        self.filterTerms['energy_filter']['electric'] = self.electricBool.get()
        self.filterTerms['energy_filter']['water'] = self.waterBool.get()
        self.filterTerms['energy_filter']['psychic'] = self.psychicBool.get()
        self.filterTerms['energy_filter']['metal'] = self.metalBool.get()
        self.filterTerms['energy_filter']['fairy'] = self.fairyBool.get()
        self.filterTerms['energy_filter']['dragon'] = self.dragonBool.get()

        self.filterTerms['set_legal']['expanded'] = self.expandBool.get()
        self.filterTerms['set_legal']['unlimited'] = self.unlimitBool.get()
        self.filterTerms['set_legal']['standard'] = self.standardBool.get()

        print(str(self.filterTerms['energy_filter']['fire']))
        if self.filterTerms['energy_filter']['fire'] == True:
            print("true fire")
    

    def select_setname(self, *args):
        self.filterTerms['set_name'] = self.searchSetName.get()
        #logstr = f'{self.filterTerms['set_name']}'
        print(self.filterTerms['set_name'])

    def clear_tree(self):
        for obwidget in self.page4.winfo_children():
            obwidget.destroy()
        print(str(obwidget) + ' destroyed')
        self.setup_tree()

    def setup_tree(self):
        column_names =('card_name', 'type', 'set_name','set_series','hp','set_legal')
        self.result_tree = ttk.Treeview(self.page4, columns=column_names, show='headings')
        self.result_tree.heading('card_name',text='Card Name')
        self.result_tree.heading('type',text='Card Type')
        self.result_tree.heading('set_name',text='Set Name')
        self.result_tree.heading('set_series',text='Set Series')
        self.result_tree.heading('hp',text='Health')
        self.result_tree.heading('set_legal',text='Deck Legal')
        self.result_tree.column('card_name',width=100,anchor=tk.W)
        self.result_tree.column('type',width=80,anchor=tk.W)
        self.result_tree.column('set_name',width=120,anchor=tk.W)
        self.result_tree.column('set_series',width=110,anchor=tk.W)
        self.result_tree.column('hp',width=100,anchor=tk.W)
        self.result_tree.column('set_legal',width=170,anchor=tk.W)
        #self.result_tree.grid(row=0,column=0,sticky='ns')
        self.result_tree.pack(side=LEFT)
        self.treeScroll = ttk.Scrollbar(self.page4,orient='vertical',command=self.result_tree.yview)
        self.treeScroll.pack(side=RIGHT, fill=Y)
        #self.treeScroll.grid(row=0,column=1,sticky='ns')

    def filter_collection(self):
        pass

    def advanced_search(self):
        pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Deck Manager - Gen 2')
        self.geometry('1000x450+250+40')
        self.resizable(True, True)
        # quit button
        self.quit_button = ttk.Button(self,text='Quit')
        self.quit_button['command'] = lambda: self.quit()
        self.quit_button.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)


if __name__ == "__main__":
    app = App()
    TabFrame(app)
    app.mainloop()
