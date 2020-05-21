def main(dic):
    """
    This function keeps only the main ingredient in recetas.ingredientes

    """
    set_clean_list=[
                     'cabezas',
                     'cabeza',
                     'caparazon',
                     'cascara',
                     'ccs',
                     'chirlas',
                     'chorreton',
                     'chorreon',
                     'chorrito',
                     'chuchradas',
                     'clavos',
                     'clavo',
                     'cocochas',
                     'copa',
                     'cucharaditas',
                     'cucharadita',
                     'cucharadas',
                     'cucharada',
                     'cuchara,'
                     'cucharitas',
                     'dientes',
                     'diente',
                     'filetes',
                     'gramos',
                     'gramo',
                     'grandes'
                     'granos',
                     'hebras',
                     'hojas',
                     'hoja',
                     'hueso',
                     'kilos',
                     'kilo',
                     'lamprea',
                     'litros',
                     'litro',
                     'moldes',
                     'pastillas',
                     'pastilla',
                     'pellizco',
                     'pizca',
                     'punta',
                     'ramita',
                     'ramito',
                     'rama',
                     'rodajas',
                     'soletillas',
                     'tazas',
                     'taza',
                     'tinta',
                     'vasitos',
                     'vasito',
                     'vaso',
                     'de' ]
    
    for e in set_clean_list:
        for i in dic.values():
            for key,value in i.items():
                if e in key:
                    new_value=key.replace(e, "").strip() 
                    i[new_value]=i.pop(key)
                    

    return dic