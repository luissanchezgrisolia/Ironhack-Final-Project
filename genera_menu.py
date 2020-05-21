import pymongo
import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
import numpy as np
from standardization import standard
from keywords import main
from user_preferences import user_pre
from scipy.spatial.distance import pdist, squareform
from modifica_platos import mod
from lista import crea_lista
from genera_recetas import crea_recetas



#BBDD

client=pymongo.MongoClient("mongodb://localhost/ComprApp")

#Collections
mydb = client.get_database()
userColl = mydb['usuarios']
recetasColl = mydb['recetas']        


#Checking if the user is already created in the user collection
userName=str(input(f"Por favor, introduce un nombre de usuario para poder empezar: "))
while not userColl.find_one({'usuario':userName}): 
    print("Lo sentimos, aún no tienes un perfil creado. Puedes hacerte uno ejecutando el fichero:'crea_usuario'")
    userName=str(input(f"Prueba con otro usuario que ya exista, por favor: "))

print(f"¡Hola {userName}! Vamos a generar tu menú y tu lista de la compra de esta semana")

try: 
    a=int(input (f"¿Cuanto tiempo -en min- como máximo te gustaría cocinar?: "))
except:
    print("Ooops, algo no ha ido bien, intentemos de nuevo")
    a=int(input (f"¿Cuanto tiempo -en min- te gustaría cocinar?: "))

b=str(input (f"Perfecto! Ahora dinos, por favor, ¿qué nivel de kcal te gustaría -Alto/Medio/Bajo-?: "))
while b!= "Alto" and b!= "Bajo" and b!= "Medio":
    print("Ooops, algo no ha ido bien, intentemos de nuevo. Recuerda que tienes que elegir entre Alto, Medio y Bajo")
    b=str(input (f"¿Qué nivel de kcal te gustaría -Alto/Medio/Bajo-?: "))

c=str(input (f"Genial! Estamos acabando, ¿te gustaría que tu recetas fuesen vegetarianas?: "))
while c!= "Si" and c!= "No":
    print("Lo sentimos pero algo no ha ido bien, intentemos de nuevo. Recuerda que tienes que elegir entre 'Si' o 'No'")
    c=str(input (f"¿Te gustaría que tu recetas fuesen vegetarianas?: "))

dislikes=[]
pregunta=input(f"Última pregunta, ¿hay algún ingrediente que no te apetezca esta semana?: ")
if pregunta== "No":
    pass
else:
    ing=str(input(f"¿Cúal?: "))
    dislikes.append(ing)
    p=str(input(f"¿Alguno más?: "))
    while p!= "No":
        dislikes.append(p)
        p=str(input(f"¿Alguno más?: "))
    else:
        print(f"¡Tomamos nota {userName}!.Estamos generando tu menú, un momento por favor")



#Connecting to database with users preferences
killer_query= {"$and":[{"tiempo":{"$lte":a}},{"kcal":b},{"vegetariana":c}]}
data= mydb.recetas.find(killer_query, { "_id":0, "nombre":1,"ingredientes":1})

#As a df
df_temp=pd.DataFrame(data)

dic_new={}
for indx,row in df_temp.iterrows():
    try:
        dic_new[row.nombre]=dict([x.split(" ",1)[::-1] for x in row.ingredientes.split("\n")])
    except:
        pass

#Standardizing measurement units. -Imported function-
standard_dic=standard(dic_new)

#Keeping only main words. -Imported function -
clean_dic_t=main(standard_dic)
try:
    clean_dic=main(clean_dic_t)
except:
    clean_dic=main(clean_dic_t)

#As a Dataframe:
sr=pd.DataFrame(clean_dic).fillna(0).T  

user_pre(sr,userName,dislikes)

#Similarity matrix cosine_similarity
s_matrix = distance(sr,sr)
sim_df = pd.DataFrame(s_matrix, columns=sr.index.values, index=sr.index.values)
top = dict(sim_df[userName].sort_values()[0:25])

#Getting all valorations
data= mydb.valoraciones.find({} , { "_id":0})  
#As a df
df=pd.DataFrame(list(data)).T
#Users as headers
df=df.rename(columns=df.iloc[0])               
df=df.drop(df.index[0])
#Filling Na
df.fillna(0, inplace=True)                     

#Distances bt user as df
distances = pd.DataFrame(1/(1 + squareform(pdist(df.T, 'euclidean'))),    
                        index=df.columns, columns=df.columns)
#Dropping itself (because one to oneself is always the max pt.)
similarities = distances[userName].sort_values(ascending=False)[1:]  

#Fitting to previus recommender system´s list
eliminar = [x for x in df.index if x not in top.keys()]                   
filter_df=df.drop(e for e in eliminar)

#Pondering recipes
recommendations = filter_df.copy()
for name, score in similarities.items():
    recommendations[name] = filter_df[name] * score

recommendations["Puntuación según tus preferencias"] = recommendations.sum(axis=1)
menu=recommendations.sort_values('Puntuación según tus preferencias', ascending=False)["Puntuación según tus preferencias"]
re_df=pd.DataFrame(menu)

print(re_df.head(5))

#Modifing user menu if required. -Imported function-
mod(re_df,userName)

#Generating the shopping list -Imported function-
crea_lista(re_df, clean_dic)

#Generating recipes -Imported function-
crea_recetas(re_df)





