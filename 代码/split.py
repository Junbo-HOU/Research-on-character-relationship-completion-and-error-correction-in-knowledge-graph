# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:46:34 2021

@author: hp
"""

import pandas as pd
from openpyxl import load_workbook
df1 = pd.read_excel(r'C:\Users\hp\Desktop\中文\merge.xlsx',usecols='A:E')
df2 = pd.read_excel(r'C:\Users\hp\Desktop\中文\merge.xlsx',usecols='A:D')
for indexs in df1.index:
    if df1.loc[indexs, 'edgename'] == '子女':
        if df1.loc[indexs,'tsex'] == '男':
            df2.loc[indexs, 'edgename'] = '儿子'
        if df1.loc[indexs,'tsex'] == '女':
            df2.loc[indexs, 'edgename'] = '女儿'
    if df1.loc[indexs, 'edgename'] == '父母':
        if df1.loc[indexs,'tsex'] == '男':
            df2.loc[indexs, 'edgename'] = '父亲'
        if df1.loc[indexs,'tsex'] == '女':
            df2.loc[indexs, 'edgename'] = '母亲'
    if df1.loc[indexs, 'edgename'] == '兄妹':
        if df1.loc[indexs,'tsex'] == '男':
            df2.loc[indexs, 'edgename'] = '兄'
        if df1.loc[indexs,'tsex'] == '女':
            df2.loc[indexs, 'edgename'] = '妹'
df2.dropna(axis=0, how='any', inplace=True)
print(df2)
writer = pd.ExcelWriter(r'C:\Users\hp\Desktop\中文\split.xlsx', engine='openpyxl')
df2.to_excel(writer)
writer.save()