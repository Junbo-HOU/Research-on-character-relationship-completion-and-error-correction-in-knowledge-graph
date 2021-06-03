import pandas as pd
from openpyxl import load_workbook
df1 = pd.read_excel(r'C:\Users\hp\Desktop\中文\final.xlsx')
for indexs in df1.index:
    if df1.loc[indexs, 'edgename'] == '儿子':
        if df1.loc[indexs, 'tsex'] == '男':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '父亲':
        if df1.loc[indexs, 'tsex'] == '男':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '兄':
        if df1.loc[indexs, 'tsex'] == '男':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '弟':
        if df1.loc[indexs, 'tsex'] == '男':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '女儿':
        if df1.loc[indexs, 'tsex'] == '女':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '母亲':
        if df1.loc[indexs, 'tsex'] == '女':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '妹':
        if df1.loc[indexs, 'tsex'] == '女':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '曾爷爷':
        if df1.loc[indexs, 'tsex'] == '男':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '曾奶奶':
        if df1.loc[indexs, 'tsex'] == '女':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '外婆':
        if df1.loc[indexs, 'tsex'] == '女':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '外公':
        if df1.loc[indexs, 'tsex'] == '女':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '奶奶':
        if df1.loc[indexs, 'tsex'] == '女':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
    if df1.loc[indexs, 'edgename'] == '爷爷':
        if df1.loc[indexs, 'tsex'] == '男':
            df1.loc[indexs, 'judge'] = 'TRUE'
        else:
            df1.loc[indexs, 'judge'] = 'FALSE'
print(df1)