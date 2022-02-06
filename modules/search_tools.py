if __name__ == "__main__":
    pass

import math
import numpy as np
#import pandas as pd
import requests
import json
import re
from config import ROOT_DIR
import os

def load_card_data():
    with open(os.path.join(ROOT_DIR,'data','cards.json'),"r") as cards_file:
            cards_obj = json.load(cards_file)
    card_data = cards_obj['data']
    return card_data

def energy_filter(filters, data_cluster):
    energy_result = []
    for individual in data_cluster:
        if filters['energy_filter']['dark'] in individual['types'] or filters['energy_filter']['fighting'] in individual['types'] or filters['energy_filter']['grass'] in individual['types'] or filters['energy_filter']['electric'] in individual['types'] or filters['energy_filter']['water'] in individual['types'] or filters['energy_filter']['psychic'] in individual['types'] or filters['energy_filter']['metal'] in individual['types'] or filters['energy_filter']['fairy'] in individual['types'] or filters['energy_filter']['dragon'] in individual['types'] or filters['energy_filter']['colorless'] in individual['types']:
            energy_result.append(individual)
    return energy_result

def ability_advanced(filters, data_cluster):
    ability_result = []
    if filters['ability_search'] != "empty_value":
        for oneCard in data_cluster:
            if "abilities" in oneCard:
                card_ = oneCard['abilities']['name'].lower().find(filters['ability_search'].lower())
                if card_ >= 0:
                    ability_result.append(oneCard)
        return ability_result
    else:
        return data_cluster

def name_advanced(filters, data_cluster):
    name_result = []
    if filters['name_search'] != "empty_value":
        for oneCard in data_cluster:
            card_ = oneCard['name'].lower().find(filters['name_search'].lower())
            if card_ >= 0:
                name_result.append(oneCard)
        return name_result
    else:
        return data_cluster

def set_filter_advanced(filters, data_cluster):
    set_result = []
    if filters['set_name'] != "All":
        for oneCard in data_cluster:
            if oneCard['set']['name'] == filters['set_name']:
                name_result.append(oneCard)
        return name_result
    else:
        return data_cluster

def legal_advanced(filters, data_cluster):
    legal_result = []
    if filters['set_legal']['expanded'] or filters['set_legal']['unlimited'] or filters['set_legal']['standard']:
        for oneCard in data_cluster:
            if "expanded" in oneCard['legalities'] or "unlimited" in oneCard['legalities'] or "standard" in oneCard['legalities']:
                legal_result.append(oneCard)
        return legal_result
    else:
        return data_cluster



def calculate_hp_advance(comparison, data_cluster, hp_value):
    calc_result = []
    if hp_value != "empty_value":
        if comparison == 'GT':
            for oneCard in data_cluster:
                if len(oneCard['hp']) > 0:
                    if int(oneCard['hp']) > hp_value:
                        calc_result.append(oneCard)
        elif comparison == 'LT':
            for oneCard in data_cluster:
                if len(oneCard['hp']) > 0:
                    if int(oneCard['hp']) < hp_value:
                        calc_result.append(oneCard)
        elif comparison == 'EQ':
            for oneCard in data_cluster:
                if len(oneCard['hp']) > 0:
                    if int(oneCard['hp']) == hp_value:
                        calc_result.append(oneCard)
        return calc_result
    else:
        return data_cluster

def name_search(cards,search_string):
    result = []
    for oneCard in cards:
        card_ = oneCard['name'].lower().find(search_string.lower())
        if card_ >= 0:
            result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'hp':oneCard['hp'],'setName':oneCard['set']['name'],'setSeries':oneCard['set']['series'],'setLegal':oneCard['set']['legalities'],'small_img':oneCard['images']['small']})
    return result

def has_abilities(cards,isAbility):
    result = []
    for oneCard in cards:
        if 'abilities' in oneCard:
            result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'ability':oneCard['abilities']['name'],'ability_text':oneCard['abilities']['text'],'ability_type':oneCard['abilities']['type']})
    return result

def search_attack(cards,search_term):
    result = []
    for oneCard in cards:
        if 'attacks' in oneCard:
            result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'attack':oneCard['attacks']['name'],'attack_cost':oneCard['attacks']['cost'],'attack_conv_cost':oneCard['attacks']['convertedEnergyCost'],'attack_damage':oneCard['attacks']['damage'],'attack_text':oneCard['attacks']['cost']})
    return result

def search_ability_names(cards,search_term):
    result = []
    for oneCard in cards:
        if 'abilities' in oneCard:
            card_ = oneCard['abilities']['name'].lower().find(search_term.lower())
            if card_ >= 0:
                result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'ability':oneCard['abilities']['name'],'ability_text':oneCard['abilities']['text'],'ability_type':oneCard['abilities']['type']})
    return result

def advanced_search(filterdict,search_term):
    card_full = load_card_data()
    set_data = set_filter_advanced(filterdict, card_full)
    energy_data = energy_filter(filterdict, set_data)
    legal_data = legal_advanced(filterdict, energy_data)
    #hp_data = calculate_hp_advance(filterdict)


