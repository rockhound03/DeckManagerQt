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

#https://doc.qt.io/qtforpython/quickstart.html
#https://www.pythontutorial.net/tkinter/

basePg = tk.Tk()
basePg.title('Deck Manager - Gen 1')
basePg.geometry('700x450+300+40')
basePg.grid()
catalog = ttk.Notebook(basePg)
catalog.grid(column=0,row=1,columnspan=2,rowspan=2,sticky=tk.SW)
pageWidth = 550
pageHeight = 280

# variable setup
fireBool = tk.BooleanVar()
darkBool = tk.BooleanVar()
electricBool = tk.BooleanVar()
grassBool = tk.BooleanVar()
waterBool = tk.BooleanVar()
psychicBool = tk.BooleanVar()
fightBool = tk.BooleanVar()
metalBool = tk.BooleanVar()
searchVar = tk.StringVar()
#result_list = []
# Setup tabs
page1 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page2 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page3 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)
page4 = ttk.Frame(catalog, width=pageWidth, height=pageHeight)

catalog.add(page1, text='Set Management')
catalog.add(page2, text='Deck Management')
catalog.add(page3, text='Database Search')
catalog.add(page4, text='Result List')
#main window buttons and labels
txt_update='Status: Idle'
status_label = Label(basePg,text=txt_update)


def status_callback():
    txt_update = 'Status: searching database'
    status_label.config(text='Status: searching database')

def filter_ckbox_callback():
    pass

exit_button = ttk.Button(
    basePg,
    text='Exit',
    command=lambda: basePg.quit()
)

updateDb_button = ttk.Button(
    basePg,
    text='Update DB',
    command=status_callback

)

#Search page ---



# Search: setup filter check boxes


filterBox = ttk.LabelFrame(page3,text='Search Filters')
filterBox.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# fire
fire_ckbox = ttk.Checkbutton(filterBox,
                                text='Fire',
                                command=filter_ckbox_callback,
                                variable=fireBool,
                                onvalue=True,
                                offvalue=False
                                )
fire_ckbox.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# dark
dark_ckbox = ttk.Checkbutton(filterBox,
                                text='Dark',
                                command=filter_ckbox_callback,
                                variable=darkBool,
                                onvalue=True,
                                offvalue=False
                                )
dark_ckbox.grid(column=1,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# fighting
fight_ckbox = ttk.Checkbutton(filterBox,
                                text='Fighting',
                                command=filter_ckbox_callback,
                                variable=fightBool,
                                onvalue=True,
                                offvalue=False
                                )
fight_ckbox.grid(column=2,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# grass
grass_ckbox = ttk.Checkbutton(filterBox,
                                text='Grass',
                                command=filter_ckbox_callback,
                                variable=grassBool,
                                onvalue=True,
                                offvalue=False
                                )
grass_ckbox.grid(column=3,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# electric
electric_ckbox = ttk.Checkbutton(filterBox,
                                text='Electric',
                                command=filter_ckbox_callback,
                                variable=electricBool,
                                onvalue=True,
                                offvalue=False
                                )
electric_ckbox.grid(column=4,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# water
water_ckbox = ttk.Checkbutton(filterBox,
                                text='Water',
                                command=filter_ckbox_callback,
                                variable=waterBool,
                                onvalue=True,
                                offvalue=False
                                )
water_ckbox.grid(column=5,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# psychic
psychic_ckbox = ttk.Checkbutton(filterBox,
                                text='Psychic',
                                command=filter_ckbox_callback,
                                variable=psychicBool,
                                onvalue=True,
                                offvalue=False
                                )
psychic_ckbox.grid(column=6,row=0,columnspan=1,rowspan=1,sticky=tk.W)
# metal
metal_ckbox = ttk.Checkbutton(filterBox,
                                text='Metal',
                                command=filter_ckbox_callback,
                                variable=metalBool,
                                onvalue=True,
                                offvalue=False
                                )
metal_ckbox.grid(column=7,row=0,columnspan=1,rowspan=1,sticky=tk.W)

# ***************************************************************
# ---------- Search Results ------------------------------------
def search_result_list(result_data):
    column_names =('card_name', 'type', 'set_name','set_series','hp','set_legal')
    tree = ttk.Treeview(page4, columns=column_names, show='headings')

    tree.heading('card_name',text='Card Name')
    tree.heading('type',text='Card Type')
    tree.heading('set_name',text='Set Name')
    tree.heading('set_series',text='Set Series')
    tree.heading('hp',text='Health')
    tree.heading('set_legal',text='Deck Legal')
    card_results = []
    for result in result_data:
        card_results.append((result['name'],result['supertype'],result['setName'],result['setSeries'],result['hp'],result['setLegal']))

    for card_result in card_results:
        tree.insert('', tk.END, values=card_result)

    tree.pack()
# searchVar
def search_callback():
    with open(os.path.join(ROOT_DIR,'data','cards.json'),"r") as cards_file:
        cards_obj = json.load(cards_file)
    cards = cards_obj['data']

    search_item = search_entry.get()
    #result_list.clear()
    result_list = search_tools.name_search(cards, search_item)
    search_result_list(result_list)
    counter = 0
    for result in result_list:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0')] # to avoid 403: Forbidden error
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(result['small_img'],'card.png')
        img = Image.open("card.png")
        py_img = ImageTk.PhotoImage(img)
        test_label = ttk.Label(resultBox,text=result['name'],image=py_img)
        test_label.configure(image=py_img)
        test_label.image = py_img
        test_label.pack()
        #test_label.grid(column=0,row=counter+2,columnspan=2,rowspan=1,sticky=tk.W)
        counter += 1


search_button = ttk.Button(
    page3,
    text='Search For:??',
    command=search_callback
)

search_entry = ttk.Entry(page3, textvariable=searchVar)
resultBox = ttk.LabelFrame(page3,text='*** Search Results ***')
#result_list.append('Search results can be found here')

# add page with treeview (branch = treeview)
exit_button.grid(column=0,row=0,columnspan=1,rowspan=1,sticky=tk.W)
updateDb_button.grid(column=1,row=0,columnspan=1,rowspan=1,sticky=tk.W)
status_label.grid(column=4,row=0,columnspan=2,rowspan=1,sticky=tk.W)
# Search page buttons
search_button.grid(column=0,row=1,columnspan=1,rowspan=1,sticky=tk.W)
search_entry.grid(column=1,row=1,columnspan=1,rowspan=1,sticky=tk.W,padx=5, pady=5)
resultBox.grid(column=0,row=2,columnspan=1,rowspan=1,sticky=tk.W)

basePg.mainloop()