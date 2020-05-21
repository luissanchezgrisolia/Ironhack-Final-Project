import pymongo

#BBDD
client=pymongo.MongoClient("mongodb://localhost/ComprApp")

#Collections
mydb = client.get_database()
userColl = mydb['usuarios']
recetasColl = mydb['recetas']   

nombre=str(input (f"Hola! Vamos a crear un usuario nuevo, por favor, ¿cúal es tu nombre? "))
userName=str(input (f"¿Cuál quieres que sea tu nombre de usuario? "))

while userColl.find_one({'usuario':userName}):
    print('El usuario ya existe, prueba con otro nombre de usuario por favor')
    userName=str(input (f"¿Cuál quieres que sea tu nombre de usuario? "))

dic = {
        "nombre": nombre,
        "usuario": userName }

userColl.insert_one(dic)
print(f'Usuario {userName} creado correctamente!')


