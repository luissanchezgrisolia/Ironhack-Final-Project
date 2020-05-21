
#Creating a function that standardizes the differents measurement units to grams


import pandas as pd
import regex as re
"""
#recipes dataset
recetas=pd.read_csv("Input/Recetas.csv")

#dictionary
new_dic={}
for index,row in recetas.iterrows():
    try:
        new_dic[row.nombre]=dict([x.split(" ",1)[::-1] for x in row.ingredientes.split("\n")])
    except:
        pass
        #print([x.split(" ",1)[::-1] for x in row.ingredientes.split("\n")])

#Making a set of all measurement unit
new_list=[]
for e in new_dic.values():
    for i in e.keys():
        new_list.append(re.findall(r"(?:^|(?:[.!?]\s))(\w+)",i))

#Clean set
clean_list=[]
for e in new_list:
    for i in e:
        clean_list.append(i)
standardize=set(clean_list)"""


def standard(dic):
    """
    This function, given a set of all measurement units, standardizes them to grams

    """

    standardize={
        'alcachofas':200,
        'apio': 400,
        'berenjena': 180,
        'berenjenas': 180,
        'cabeza': 150,
       #'cabezas': 150,
        'calabacin': 200,
        'cebolla': 75,
        'cebolletas': 75,
        'chorreon': 10,
        'chorreton': 10,
        'chorrito': 5,
        'chuchradas':10,
       # 'cigalas': 80,
        'clavo': 3,
        'clavos': 3,
        'cocochas': 70,
        'codornices': 80,
        'copa':100,
        'diente': 15,
       #'dientes': 15,
        'espárragos':40,
        'filetes':100,
       # 'gambas':20,
        'guindilla':10,
       #'guindillas':10,
        'huevo': 60,
       #'huevos': 60,
        'kilo': 1000,
       #'kilos': 1000,
       #'limones': 75,
        'limón': 75,
        'manzana': 100,
        'merluza': 200,
        'naranjas':120,
        'pastilla':10,
        'patatas':120,
        'pellizco':2,
        'pimiento':120,
       #'pimientos':120,
        'pizca': 2,
        'puerro':100 ,
       #'puerros': 100,
        'tazas': 200,
        'tomate': 100,
       #'tomates': 150,
        'vasito': 200,
       #'vasitos': 200,
        'vaso': 200,
        'zanahorias': 100
        }
    
    for e in standardize:
        for i in dic.values():
            for key,value in i.items():
                if e in key:
                    i[key] = float(value)*float(standardize[e])
    return dic