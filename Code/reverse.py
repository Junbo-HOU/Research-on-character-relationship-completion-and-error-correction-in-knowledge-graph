# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:39:13 2021

@author: hp
"""
import pandas as pd
from openpyxl import load_workbook
df1 = pd.read_excel(r'C:\Users\hp\Desktop\中文\original.xlsx',usecols='A:E')
df3 = pd.read_excel(r'C:\Users\hp\Desktop\中文\original.xlsx',usecols='A:D')
for indexs in df3.index:
    if df1.loc[indexs, 'edgename'] == '妻':
        df3.loc[indexs, 'edgename'] = '夫'
    if df1.loc[indexs, 'edgename'] == '夫':
        df3.loc[indexs, 'edgename'] = '妻'
    if df1.loc[indexs, 'edgename'] == '儿子':
        if df1.loc[indexs,'hsex'] == '男':
            df3.loc[indexs, 'edgename'] = '父亲'
        if df1.loc[indexs,'tsex'] == '女':
            df3.loc[indexs, 'edgename'] = '母亲'
    if df1.loc[indexs, 'edgename'] == '女儿':
        if df1.loc[indexs,'hsex'] == '男':
            df3.loc[indexs, 'edgename'] = '父亲'
        if df1.loc[indexs,'tsex'] == '女':
            df3.loc[indexs, 'edgename'] = '母亲'
    if df1.loc[indexs, 'edgename'] == '父亲':
        if df1.loc[indexs,'tsex'] == '男':
            df3.loc[indexs, 'edgename'] = '儿子'
        if df1.loc[indexs,'tsex'] == '女':
            df3.loc[indexs, 'edgename'] = '女儿'
    if df1.loc[indexs, 'edgename'] == '母亲':
        if df1.loc[indexs,'tsex'] == '女':
            df3.loc[indexs, 'edgename'] = '女儿'
        if df1.loc[indexs,'tsex'] == '男':
            df3.loc[indexs, 'edgename'] = '儿子'
df3.dropna(axis=0, how='any', inplace=True)
writer = pd.ExcelWriter(r'C:\Users\hp\Desktop\中文\reverse.xlsx', engine='openpyxl')
df3.to_excel(writer)
writer.save()