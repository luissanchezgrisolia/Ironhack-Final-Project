import pandas as pd
import request
from pymongo import MongoClient
import pymongo

#BBDD

client=pymongo.MongoClient("mongodb://localhost/ComprApp")

#Collections
mydb = client.get_database()
userColl = mydb['usuarios']
recetasColl = mydb['recetas']  

def crea_recetas(df):
    """
    This function generates the selected recipes explanation
    """

    #Getting all recipes
    datas= mydb.recetas.find({} , { "_id":0,"nombre":1,"receta":1})  

    #As a df
    df_recetas=pd.DataFrame(list(datas))

    #Setting new index
    df_recetas.set_index(["nombre"],inplace=True)

    #Iterating to get the recipes
    for e in df_recetas.index:
        if e in df.head(5).index:
                print(df_recetas.loc[e])

    return df_recetas