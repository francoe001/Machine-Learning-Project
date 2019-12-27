#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:50:33 2019

@author: efrancois
"""

import pandas as pd
from flask import request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process, fuzz
import pickle


rec_group = pd.read_csv('../data/rec_group.csv', index_col = 'artist')

#query =input('Enter Artist NAme: ')

def make_recommendations(query): 
    fixed_query = process.extractOne(query, rec_group.index,scorer=fuzz.token_sort_ratio)[0]
    if query==fixed_query:
        print('Artist found! Matching on {}'.format(query))
    else:
        print('{} not found! Matching on {} instead'.format(query,fixed_query))
    
    
    match = rec_group[rec_group.index==fixed_query]
    
    match
    rest_of_entries = rec_group[rec_group.index!=fixed_query]
    
    if match.empty:\
        print('Not Found!')
    
    rest_of_entries['Dist'] = cosine_similarity(match, rest_of_entries)[0,:]
    
    return rest_of_entries.sort_values('Dist', ascending = False).head(2).index

#
## Saving model to disk
#pickle.dump(cosine_similarity, open('model.pkl','wb'))
#
## Loading model to compare the results
#model = pickle.load(open('model.pkl','rb'))



#def get_recs():
#   
#    data= request.json
#    print(data)
#    print(request.form)
#    query=request.form['artist']
#    
#    fixed_query = process.extractOne(query, rec_group.index,scorer=fuzz.token_sort_ratio)[0]
#    if query==fixed_query:
#        print('Artist found! Matching on {}'.format(query))
#    else:
#        print('{} not found! Matching on {} instead'.format(query,fixed_query))
#    
#    
#    match = rec_group[rec_group.index==fixed_query]
#    
#    match
#    rest_of_entries = rec_group[rec_group.index!=fixed_query]
#    
#    if match.empty:\
#        print('Not Found!')
#    
#    rest_of_entries['Dist'] = cosine_similarity(match, rest_of_entries)[0,:]
#    
#    return jsonify(list(rest_of_entries.sort_values('Dist', ascending = False).head(20).index))



