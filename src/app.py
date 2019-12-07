#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:11:11 2019

@author: efrancois
"""
import pandas as pd
import flask
from flask import request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process, fuzz
 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

rec_group = pd.read_csv('../data/rec_group.csv', index_col = 'artist')



@app.route('/recs', methods=['POST'])
def get_recs():
   
    data= request.json
    print(data)
    print(request.form)
    query=request.form['artist']
    
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
    
    return jsonify(list(rest_of_entries.sort_values('Dist', ascending = False).head(20).index))
    
    

if __name__ == '__main_':
    rec_group = pd.read_csv('../data/rec_group.csv', index_col = 'artist')
    print(rec_group.shape)

    app.run(port=5000)