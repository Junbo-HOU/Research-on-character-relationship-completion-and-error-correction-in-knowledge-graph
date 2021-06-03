import pprint
import copy
import xlrd
import xlwt
book = xlrd.open_workbook(r"C:\Users\hp\Desktop\中文\original1.xlsx")
list2 = book.sheet_by_name('original')
name =  list2.col_values(0)
name1 = []
for item in name:  #name去重
    if item not in name1:
        name1.append(item)
#print(name)
roriginal = {}
for object in name1:   #遍历name 
    pdict = {}
    rela_val = []
    #for object in name:
    #l2 = list()
    #取出所有人物关系的名称
    relation = []   #人物关系的名称
    for i in range(list2.nrows-1):   
        row = list2.row_values(i)   #提取list2的每一行， row是列表里所有的值
        #print(row)
        if row[0] == object:       #判断是否是同一个人，如果是同一个人，就把他所有的关系加进去 row【1】
            relation.append(row[1])
    s1 = []
    for item in relation:
        if not item in s1:
            s1.append(item)      #relation去重
    j = 0
        #print(s1)
    while j < len(s1):
        tu = []        #把关系和人物装到一个列表里
        l1=[i for i, x in enumerate(relation) if x == s1[j]]   #找这个人具有相同关系的所有的关系的下标
        for item in l1:
            row = list2.row_values(name.index(object)+item)
            tu.append(row[2])    #把具有相同关系的人物加一个列表里
        rela_val.append(tuple([row[1],tu]))
        j += 1
        pdict.update(rela_val)   #改成以字典形式输出
       # if object == '李守中':
          #  print(pdict)
        roriginal[object] = pdict       #将pdict与人物对应，以字典形式输出
#pprint.pprint(roriginal)
##for item1,item2 in big_dict.items():
#    #print(item1,":",item2)
d = {"父亲":{"父亲":"爷爷","爷爷":"曾爷爷","母亲":"奶奶","奶奶":"曾奶奶","妹":"姑姑","弟":"叔叔","兄":"大伯"},
    "母亲":{"父亲":"外公","母亲":"外婆","外公":"曾外公","外婆":"曾外婆","妹":"姨","弟":"舅舅","兄":"舅舅"},
    "儿子":{"儿子":"孙子","女儿":"孙女","妻":"儿媳"},
    "女儿":{"儿子":"外孙","女儿":"外孙女","夫":"女婿"},
    "夫":{"父亲":"公公","母亲":"婆婆","弟":"小叔子","妹":"小姑子"},
    "妻":{"父亲":"岳父","母亲":"岳母","弟":"小舅子","妹":"小姨子"},
    "弟":{"儿子":"侄子","女儿":"侄女"},
    "兄":{"儿子":"侄子","女儿":"侄女"},
    "妹":{"儿子":"外甥","女儿":"外甥女"}}
def read_excel():
    #打开excel表，填写路径
    book = xlrd.open_workbook(r"C:\Users\hp\Desktop\中文\vertex.xlsx")
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
            sex = {}
            values = table.col_values(j)
            for x in range(row_Num):
                # 把key值对应的value赋值给key，每行循环
                sex[key[x]]=values[x]
            j+=1
            # 把字典加到列表中
            #s.append(d)
        return sex
sex=read_excel()
#pprint.pprint(sex)
wb = xlwt.Workbook(encoding = 'ascii')
ws = wb.add_sheet('transfer')
ws.write(0,0,label= 'head')
ws.write(0,1,label= 'hsex')
ws.write(0,2,label= 'tail')
ws.write(0,3,label= 'tsex')
ws.write(0,4,label= 'edgename')
ws.write(0,5,label= 'mark')
count = 1
i = 1
j = 1
r = roriginal
while(count > 0):
    count = 0
    rall = copy.deepcopy(r)
    for name1, rv1 in r.items():     #name1第一个主体人物的名字   name1主体对应的字典  r.items() 字典里面的值
        print(rv1)
#        print(r.items())
        for r1, name2_list in rv1.items():  #r1 name1主体对应的关系， name2list是主体rv1字典中的人物列表
            for name2 in name2_list:         #遍历
                if name2 not in r.keys():   #判断关系人物也是主体人物
                    continue
                for r2, name3_list in r[name2].items():         #r2是主体对应关系
                    if r1 in d and r2 in d[r1]:  #转换新关系
                        rnew = d[r1][r2]
                        name3_rall=[]      #所有关系后的主体
                        #name3_rall.clear
                        for name3 in name3_list:
                            if name1 in rall and rnew in rall[name1] and name3 in rall[name1][rnew]:
                                continue
                            #if i == 2:
                                #print(r[name1])
#                            print(name1,'\t',sex[name1],'\t', name3,'\t', sex[name3],'\t',rnew,'\t',"transfer"+str(i))
                            ws.write(j,0,label = name1)
                            ws.write(j,1,label = sex[name1])
                            ws.write(j,2,label = name3)
                            ws.write(j,3,label = sex[name3])
                            ws.write(j,4,label = rnew)
                            ws.write(j,5,label = 'transfer'+str(i))
                            j += 1
                            name3_rall.append(name3)     #转换后的人的列表
                            count = count + 1
#                            print(count)
                        if name3_rall:
                            rall.setdefault(name1, {})
                            rall[name1].setdefault(rnew, []).extend(name3_rall)
#                            #print(name3_rall)                        
#            
    r = rall
    i = i + 1
#wb.save('./transfer.xls')
#pprint.pprint(r)
