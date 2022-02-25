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

def parse_results_variable(result_type, result_array):
    pass
    '''parsed_results = []
    if result_type == "attacks":
        attack_name = []
        energy_cost = []
        damage = []
        attack_text []

        for l in result_array:
            if 'cost' in l:
                chip = l.split(', ')
                attack_name.append(chip[0])
            if 'convertedEnergyCost' in l:
                energy_list = l.strip('[').strip(']')
    '''            