if __name__ == "__main__":
    pass

import sys
import os
import json
import tkinter as tk
from config import ROOT_DIR

def filter_bool_init():
    filters = {
        "energy_filter":{
            "fire" : "empty_value",
            "dark" : "empty_value",
            "fighting" : "empty_value",
            "grass" : "empty_value",
            "electric" : "empty_value",
            "water" : "empty_value",
            "psychic" : "empty_value",
            "metal" : "empty_value",
            "fairy" : "empty_value",
            "dragon" : "empty_value",
            "colorless" : "empty_value"
            },
        "set_legal":{
            "expanded" : False,
            "unlimited" : False,
            "standard" : False
            },
        "set_name" : "All",
        "name_search" : "empty_value",
        "ability_search" : "empty_value",
        "hp_search" : "empty_value"
        }
    return filters

def load_set_names():
    with open(os.path.join(ROOT_DIR,'data','sets.json'),"r") as cards_file:
            cards_obj = json.load(cards_file)
    sets = cards_obj['data']
    set_list = []
    set_list.append('All')
    for one_set in sets:
        set_list.append(one_set['name'])
    return set_list