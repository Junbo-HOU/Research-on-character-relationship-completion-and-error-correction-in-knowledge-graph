# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:12:15 2021

@author: hp
"""

import pandas as pd
from openpyxl import load_workbook
df1 = pd.read_excel(r'C:\Users\hp\Desktop\中文\original.xlsx')
df2 = pd.read_excel(r'C:\Users\hp\Desktop\中文\merge.xlsx')
df3 = pd.read_excel(r'C:\Users\hp\Desktop\中文\reverse.xlsx')
df4 = pd.concat([df1,df2,df3]) 
writer = pd.ExcelWriter(r'C:\Users\hp\Desktop\中文\final.xlsx', engine='openpyxl')
df4.to_excel(writer)
writer.save()
df5 = pd.read_excel(r'C:\Users\hp\Desktop\中文\mergeoriginal.xlsx')
df6 = pd.read_excel(r'C:\Users\hp\Desktop\中文\split.xlsx')
df7= pd.concat([df5,df6]) 
writer = pd.ExcelWriter(r'C:\Users\hp\Desktop\中文\final2.xlsx', engine='openpyxl')
df7.to_excel(writer)
writer.save()