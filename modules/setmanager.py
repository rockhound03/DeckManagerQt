if __name__ == "__main__":
    pass

import math
import numpy as np
import pandas as pd
import requests
import json

def load_set_list():
    try:
        with open("sets.json","r") as sets_file:
            temp_obj = json.load(sets_file)
            result = temp_obj['data']
    except:
        result = "Failed to read set list."
    return result

def load_card_list():
    try:
        with open("cards.json","r") as cards_file:
            temp_obj = json.load(cards_file)
            result = temp_obj['data']
    except:
        result = "Failed to read card list."
    return result
