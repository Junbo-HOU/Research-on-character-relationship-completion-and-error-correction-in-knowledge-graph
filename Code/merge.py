# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:46:22 2021

@author: hp
"""

import pandas as pd
from openpyxl import load_workbook
df1 = pd.read_excel(r'C:\Users\hp\Desktop\中文\original.xlsx',usecols='A:E')
df2 = pd.read_excel(r'C:\Users\hp\Desktop\中文\original.xlsx',usecols='A:D')
#merge
for indexs in df1.index:
    if df1.loc[indexs, 'edgename'] == '儿子':
        df2.loc[indexs, 'edgename'] = '子女'
    if df1.loc[indexs, 'edgename'] == '女儿':
        df2.loc[indexs, 'edgename'] = '子女'
    if df1.loc[indexs, 'edgename'] == '母亲':
        df2.loc[indexs, 'edgename'] = '父母'
    if df1.loc[indexs, 'edgename'] == '父亲':
        df2.loc[indexs, 'edgename'] = '父母'
    if df1.loc[indexs, 'edgename'] == '妹':
        df2.loc[indexs, 'edgename'] = '兄妹'
    if df1.loc[indexs, 'edgename'] == '兄':
        df2.loc[indexs, 'edgename'] = '兄妹' 
#print(df2)
df2.dropna(axis=0, how='any', inplace=True)
writer = pd.ExcelWriter(r'C:\Users\hp\Desktop\中文\merge.xlsx', engine='openpyxl')
df2.to_excel(writer)
writer.save()
