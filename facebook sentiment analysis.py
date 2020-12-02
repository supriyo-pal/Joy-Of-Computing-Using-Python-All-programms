# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:57:29 2020

@author: Supriyo
"""
'''
download the facebook data

store it in a excel file
'''

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')
file='sentiment.xlsx'

xl=pd.ExcelFile(file)

dfs=xl.parse(xl.sheet_names[0])#parsing the exel sheet to dataframe
dfs=list(dfs)#removes the blank rows from the data frame
print(dfs)

sid=SentimentIntensityAnalyzer()
str1="UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if a==-1:
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
