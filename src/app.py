#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:11:11 2019

@author: efrancois
"""
import pandas as pd
import flask
from flask import request, jsonify, render_template, flash, session
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process, fuzz
#from model import make_recommendations
#import pickle
 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


#model = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recs', methods=['POST'])
def recommend():
    query = str(request.form.get('artist_name'))
    
    rec_group = pd.read_csv('../data/rec_group.csv', index_col = 'artist')

    fixed_query = process.extractOne(query, rec_group.index,scorer=fuzz.token_sort_ratio)[0]
    if query==fixed_query:
        flash('Artist found! Matching on {}'.format(query))
    else:
        flash('{} not found! Matching on {} instead'.format(query,fixed_query))
    
    
    match = rec_group[rec_group.index==fixed_query]
    
    match
    rest_of_entries = rec_group[rec_group.index!=fixed_query]
    
    if match.empty:\
        flash('Not Found!')
    
    rest_of_entries['Dist'] = cosine_similarity(match, rest_of_entries)[0,:]
    
    recommendations = rest_of_entries.sort_values('Dist', ascending = False).head(10).index
    
    return flask.render_template('results.html', prediction=recommendations)




   
    
    
    

if __name__ == '__main__':
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    app.run()