#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:44:33 2019

@author: efrancois
"""


import pandas as pd
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup



BASE_URL = "https://genius.com"

section_url = "https://genius.com/discussions/22873-Greatest-100-rappers"

def get_category_links(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    greatest = soup.find("div", "body embedly embedly_pro")
    category_links = [BASE_URL + li.a["href"] for li in greatest.findAll("li")]
    return category_links

print(get_category_links(section_url))





##%%
#
#search_term = 'Jay-Z'
#
#_URL_API = "https://api.genius.com/"
#
#_URL_SEARCH = "search?q="
#
#client_access_token = "lSUVIEFu57a_JUG5gUTMqPRgOUIBqNJJtSWWqaG1LnBc2FMi8qveGlBapwaTCRJe"
#
#querystring = _URL_API + _URL_SEARCH + urllib.parse.quote(search_term)
#
#req = urllib.request.urlopen(querystring)
#
#req.add_header("Authorization", "Bearer " + client_access_token)
#
#req.add_header("User-Agent", "")
#
#response = urllib.urlopen(req, timeout=3)
#
#json_obj = response.json()
#
#json_obj.viewkeys()
#
#print(json_obj['response']['hits'][0]['result'].keys())
#
##%%
#import lyricsgenius
#
#genius = lyricsgenius.Genius("lSUVIEFu57a_JUG5gUTMqPRgOUIBqNJJtSWWqaG1LnBc2FMi8qveGlBapwaTCRJe")
#artist = genius.search_artist("Jay-Z", max_songs=3, sort="title")
#
#lyric_dict = {}
#for song in artist.songs:
#    lyric_dict[song.title] = song.lyrics

