# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import scipy.stats as stats
import csv
import pandas as pd
import seaborn as sns

# this line tells jupyter notebook to put the plots in the notebook rather than saving them to file.
"%matplotlib inline"

# this line makes plots prettier on mac retina screens. If you don't have one it shouldn't do anything.
"%config InlineBackend.figure_format = 'retina'"


# Question 1
raw_data = {}
file_path = './sat_scores.csv'


# Read csv by using csv:
with open(file_path, 'r') as f:
    temp_data = csv.DictReader(f)
    
    first_attempt = True
    local_obj = {}
    for row in temp_data:
        temp_key = list(row.keys())
        temp_value = list(row.values())
        
#        print(temp_value)
        if first_attempt:
            # init dictionary with key given by temp_key
            local_obj = dict.fromkeys((temp_key),[])
            first_attempt = False
            print(local_obj.keys())
        
        count_print = 1
        for k,v in enumerate(temp_key):
            print("k:",k)
            print("v:",temp_value[k])
            print("\n")
            local_obj[v].append(temp_value[k])
            if count_print < 2:
                print(local_obj)
                count_print += 1

#        print(local_obj)
f.close()

# DEF return a dictionary with one key
"def push_ordict_to_dict(final_dict,ordered_dict):"
    
