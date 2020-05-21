
import pandas as pd
from pdf import genPDF
"""
Gicen a dic and a df, this functions generates a shopping list
"""
def crea_lista(df, dic):
    set_total_ingredientes=[
        'aceite',
        'aceitunas',
        'acelgas',
        'agua',
        'ajo',
        'ajos',
        'albahaca',
        'alcachofa',
        'alcachofas',
        'almeja',
        'almejas',
        'almendras',
        'almortas',
        'anchas',
        'anis',
        'apio',
        'arroz',
        'atun',
        'azafran',
        'azucar',
        'bacalao',
        'berenjena',
        'berenjenas',
        'besugo',
        'bogavante',
        'boquerones',
        'brandy',
        'cabrales',
        'calabacin',
        'calamar',
        'calamares',
        'callos',
        'canela',
        'carne',
        'castanas',
        'cayena',
        'cebolla',
        'cebollas',
        'cebolletas',
        'cerdo',
        'cerveza',
        'champinones',
        'chocolate',
        'chorizo',
        'chorizos',
        'ciervo',
        'cigalas',
        'cochinillo',
        'codornices',
        'coliflor',
        'colorante',
        'comino',
        'cominos',
        'conac',
        'conejo',
        'costillas',
        'dorada',
        'ensalada',
        'esparragos',
        'espinazo',
        'fabes',
        'gambas',
        'garbanzos',
        'guindilla',
        'guindillas',
        'guisantes',
        'habas',
        'harina',
        'higado',
        'huevo',
        'huevos',
        'jamon',
        'jamon,',
        'judia',
        'judias',
        'lacon',
        'laurel',
        'leche',
        'lentejas',
        'levadura',
        'limon,',
        'limones',
        'lomo',
        'lomos',
        'lubina',
        'macarrones',
        'magro',
        'maiz',
        'manteca',
        'mantequilla',
        'manzana',
        'mejilllones',
        'mejillones',
        'merluza',
        'miga',
        'morcilla',
        'naranjas',
        'nata',
        'nueces',
        'nuez',
        'oregano',
        'paletilla',
        'pan',
        'panceta',
        'patata',
        'patatas',
        'pavo',
        'pepino',
        'perejil',
        'pimenton',
        'pimienta',
        'pimiento',
        'pimientos',
        'pollo',
        'puerro',
        'puerros',
        'queso',
        'rabo',
        'rape',
        'repollo',
        'romero',
        'sal',
        'sepia',
        'setas',
        'sidra',
        'solomillo',
        'ternera',
        'tocino',
        'tomate',
        'tomates',
        'tomillo',
        'toro',
        'torrijas',
        'torta',
        'trufa',
        'verdura',
        'vinagre',
        'vino',
        'whisky',
        'zanahorias',
        'zumo']

    #Keep only the selectec recipes
    remove = [k for k in dic if k not in df.head(5).index]
    for k in remove: del dic[k]

    #Fitting the dic
    try:
        for e in set_total_ingredientes:
            for i in dic.values():
                for key,value in i.items():
                    if e in key:
                        new_value=key.replace(key, e).strip() 
                        i[new_value]=i.pop(key) 
    except:
        for e in set_total_ingredientes:
            for i in dic.values():
                for key,value in i.items():
                    if e in key:
                        new_value=key.replace(key, e).strip() 
                        i[new_value]=i.pop(key) 

 
    #Creating the final list
    dic_lista={}
    for e in set_total_ingredientes:
        for i in dic.values():
            for key,value in i.items():
                if e in key:
                    dic_lista[e]=f"{i[e]} gramos"

    #As a df
    df_lista=pd.DataFrame(dic_lista,index=[0]).T

    print(df_lista)

    
    return df_lista
