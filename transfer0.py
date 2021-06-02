# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:46:07 2021

@author: hp
"""
import pprint
import copy
import xlrd
import json
book = xlrd.open_workbook(r"C:\Users\hp\Desktop\pytest\original1.xlsx")
list2 = book.sheet_by_name('original')
name =  list2.col_values(0)
#print(name)
roriginal = {}
for object in name:
    pdict = {}
    rela_val = []
    #for object in name:
    #l2 = list()
    #取出所有人物关系的名称
    relation = []
    for i in range(list2.nrows-1):
        row = list2.row_values(i)
        #print(row)
        if row[0] == object:
            relation.append(row[1])

    s1 = []
    for item in relation:
        if not item in s1:
            s1.append(item)
    j = 0
    #print(s1)
    while j < len(s1):
        tu = []
        l1=[i for i, x in enumerate(relation) if x == s1[j]]
        for item in l1:
            row = list2.row_values(name.index(object)+item)
            tu.append(row[2])
        rela_val.append(tuple([row[1],tu]))
        j += 1
        pdict.update(rela_val)
#        print(pdict)
        roriginal[object] = pdict
#print(roriginal)
#for item1,item2 in big_dict.items():
#    print(item1,":",item2)
d = {"father":{"father":"grandfather","grandfather":"great_grandfather","mother":"grandmother","grandmother":"great_grandmother","younger_sister":"aunt","elder_sister":"aunt","younger_brother":"uncle","elder_brother":"uncle"},
    "mother":{"father":"grandfather","mother":"grandmother","younger_sister":"aunt","elder_sister":"aunt","younger_brother":"uncle","elder_brother":"uncle"},
    "son":{"son":"grandson","daughter":"granddaughter","wife":"daughter_in_law"},
    "daughter":{"son":"grandson","daughter":"granddaughter","husband":"son_in_law"},
    "husband":{"father":"father_in_law","mother":"mother_in_law","younger_brother":"brother_in_law","younger_sister":"sister_in_law"},
    "wife":{"father":"father_in_law","mother_in_law":"mother","younger_brother":"brother_in_law","younger_sister":"sister_in_law"},
    "younger_brother":{"son":"nephew","daughter":"niece"},
    "elder_brother":{"son":"nephew","daughter":"niece"},
    "elder_sister":{"son":"nephew","daughter":"niece"},
    "younger_sister":{"son":"nephew","daughter":"niece"}}
def read_excel():
    #打开excel表，填写路径
    book = xlrd.open_workbook(r"C:\Users\hp\Desktop\pytest\vertex.xlsx")
    #找到sheet页
    table = book.sheet_by_name("vertex")
    #获取总行数总列数
    row_Num = table.nrows
    col_Num = table.ncols

   # s =[]
    key =table.col_values(0)# 这是第一列数据，作为字典的key值

    if col_Num <= 1:
        print("没数据")
    else:
        j = 1
        for i in range(col_Num-1):
            d ={}
            values = table.col_values(j)
            for x in range(row_Num):
                # 把key值对应的value赋值给key，每行循环
                d[key[x]]=values[x]
            j+=1
            # 把字典加到列表中
            #s.append(d)
        return d
sex=read_excel()
#pprint.pprint(sex)
count = 1
i = 1
r = roriginal
while(count > 0):
    count = 0
    rall = copy.deepcopy(r)
    for name1, rv1 in r.items():
        for r1, name2_list in rv1.items(): 
            for name2 in name2_list:
                if name2 not in r.keys():
                    continue
                for r2, name3_list in r[name2].items():
                    if r1 in d and r2 in d[r1]:  
                        rnew = d[r1][r2]
                        name3_rall=[]
                        #name3_rall.clear
                        for name3 in name3_list:
                            if name1 in rall and rnew in rall[name1] and name3 in rall[name1][rnew]:
                                continue
                            print(name1,sex[name1] , name3, sex[name3], rnew, "transfer"+str(i))
                            name3_rall.append(name3)
                            count = count + 1
                            #print(count)
                        if name3_rall:
                            rall.setdefault(name1, {})
                            rall[name1].setdefault(rnew, []).extend(name3_rall)
                            #print(name3_rall)
                        
            
    r = rall
    i = i + 1
#pprint.pprint(r)
    