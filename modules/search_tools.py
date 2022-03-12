if __name__ == "__main__":
    pass
import sys
import math
import numpy as np
#import pandas as pd
import requests
import json
import re
from config import ROOT_DIR
import os

def load_card_data():
    with open(os.path.join(ROOT_DIR,'data','all_cards.json'),"r") as cards_file:
            cards_obj = json.load(cards_file)
    #card_data = cards_obj['data']
    card_data = cards_obj
    return card_data

def energy_filter(filters, data_cluster):
    energy_result = []
    if filters['energy_filter']['dark'] == "Darkness" or filters['energy_filter']['fighting'] == "Fighting" or filters['energy_filter']['grass'] == "Grass" or filters['energy_filter']['electric'] == "Lightning" or filters['energy_filter']['water'] == "Water" or filters['energy_filter']['psychic'] == "Psychic" or filters['energy_filter']['metal'] == "Metal" or filters['energy_filter']['fairy'] == "Fairy" or filters['energy_filter']['dragon'] == "Dragon" or filters['energy_filter']['colorless'] == "Colorless":
        for individual in data_cluster:
            if 'types' in individual:
                if filters['energy_filter']['dark'] in individual['types'] or filters['energy_filter']['fighting'] in individual['types'] or filters['energy_filter']['grass'] in individual['types'] or filters['energy_filter']['electric'] in individual['types'] or filters['energy_filter']['water'] in individual['types'] or filters['energy_filter']['psychic'] in individual['types'] or filters['energy_filter']['metal'] in individual['types'] or filters['energy_filter']['fairy'] in individual['types'] or filters['energy_filter']['dragon'] in individual['types'] or filters['energy_filter']['colorless'] in individual['types']:
                    energy_result.append(individual)
        return energy_result
    else:
        return data_cluster

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
                set_result.append(oneCard)
        return set_result
    else:
        return data_cluster

def legal_advanced(filters, data_cluster):
    legal_result = []
    if filters['set_legal']['expanded'] or filters['set_legal']['unlimited'] or filters['set_legal']['standard']:
        print("Searching for legal sets.")
        for oneCard in data_cluster:
            if filters['set_legal']['expanded']:
                if "expanded" in oneCard['legalities']:
                    print("found expanded.")
                    legal_result.append(oneCard)
            if filters['set_legal']['unlimited']:       
                if "unlimited" in oneCard['legalities']:
                    print("found unlimited.")
                    legal_result.append(oneCard)
            if filters['set_legal']['standard']:
                if "standard" in oneCard['legalities']:
                    print("found standard.")
                    legal_result.append(oneCard)
        return legal_result
    else:
        print("no legal action")
        return data_cluster



def calculate_hp_advance(comparison, data_cluster, hp_value):
    calc_result = []
    print("huh???")
    if hp_value != "empty_value":
        print("I should calc hp!!!")
        if comparison == 'GT':
            for oneCard in data_cluster:
                if len(oneCard['hp']) > 0:
                    if 'hp' in oneCard:
                        if int(oneCard['hp']) > hp_value:
                            calc_result.append(oneCard)
        elif comparison == 'LT':
            for oneCard in data_cluster:
                if len(oneCard['hp']) > 0:
                    if 'hp' in oneCard:
                        if int(oneCard['hp']) < hp_value:
                            calc_result.append(oneCard)
        elif comparison == 'EQ':
            for oneCard in data_cluster:
                if len(oneCard['hp']) > 0:
                    if 'hp' in oneCard:
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
            if 'subtypes' in oneCard:
                one_subtype = oneCard['subtypes'][0]
            else:
                one_subtype = "none"
            if 'hp' in oneCard:
                one_hp = oneCard['hp']
            else:
                one_hp = "none"
            result.append({'id':oneCard['id'],'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':one_subtype,'hp':one_hp,'setName':oneCard['set']['name'],'setSeries':oneCard['set']['series'],'setLegal':oneCard['set']['legalities'],'small_img':oneCard['images']['small']})
    return result

def has_abilities(cards,isAbility):
    result = []
    for oneCard in cards:
        if 'abilities' in oneCard:
            result.append({'id':oneCard['id'],'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'ability':oneCard['abilities']['name'],'ability_text':oneCard['abilities']['text'],'ability_type':oneCard['abilities']['type']})
    return result

def search_attack(cards,search_term):
    result = []
    for oneCard in cards:
        if 'attacks' in oneCard:
            result.append({'id':oneCard['id'],'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'attack':oneCard['attacks']['name'],'attack_cost':oneCard['attacks']['cost'],'attack_conv_cost':oneCard['attacks']['convertedEnergyCost'],'attack_damage':oneCard['attacks']['damage'],'attack_text':oneCard['attacks']['cost']})
    return result

def search_ability_names(cards,search_term):
    result = []
    for oneCard in cards:
        if 'abilities' in oneCard:
            card_ = oneCard['abilities']['name'].lower().find(search_term.lower())
            if card_ >= 0:
                result.append({'id':oneCard['id'],'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'setName':oneCard['set']['name'],'ability':oneCard['abilities']['name'],'ability_text':oneCard['abilities']['text'],'ability_type':oneCard['abilities']['type']})
    return result

def result_format_basic(cards):
    basic_result = []
    for oneCard in cards:
        basic_result.append({'id':oneCard['id'],'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'hp':oneCard['hp'],'setName':oneCard['set']['name'],'setSeries':oneCard['set']['series'],'setLegal':oneCard['set']['legalities'],'small_img':oneCard['images']['small']})
    return basic_result

def advanced_search(filterdict):
    card_full = load_card_data()
    set_data = set_filter_advanced(filterdict, card_full)
    energy_data = energy_filter(filterdict, set_data)
    name_data = name_advanced(filterdict, energy_data)
    legal_data = legal_advanced(filterdict, name_data)
    print("post legal status:")
    print(filterdict['hp_check'])
    print(filterdict['hp_search'])
    print(str(len(legal_data)))
    if filterdict['hp_search'] != "empty_value":
        hp_data = calculate_hp_advance(filterdict['hp_check'], legal_data, int(filterdict['hp_search']))
        search_results = result_format_basic(hp_data)
        print("Yes HP")
        print(str(len(search_results)))
        #return hp_data
    else:
        search_results = result_format_basic(legal_data)
        #return legal_data
        print("No HP")
        print(str(len(search_results)))
    return search_results


def advanced_setup(filter_terms):
    energy = filter_terms['energy_filter']
    bin_name = []
    for egy_type in energy:
        bin_name.append(egy_type)
    for name in bin_name:
        print(energy[name])
