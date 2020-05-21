def mod(df,userName):
    """
    Given a dataframe, this function modifies user menu preferences

    """
    confirmacion=str(input(f"Este es tu menu personalizado para esta semana, {userName} , si te gusta, por favor, confírmanoslo  para poder hacer la compra. ¿Quieres cambiar algún plato? "))
    while confirmacion == "Si":
        plato_cambio=str(input(f"¿Cúal te gustaría modificar? "))
        while plato_cambio not in df.index.values:
            plato_cambio=str(input(f"Lo sentimos {userName} , no podemos encontrar ese plato en el menú, probemos de nuevo, ¿Cúal te gustaría modificar? "))
        else:
            df.drop(plato_cambio, inplace=True)
            print("Vale, te lo hemos cambiado. Ahora tu nuevo menú es este:")
            print(df.head(5))
            confirmacion=str(input(f"Si te gusta, por favor, confírmanoslo  para poder hacer la compra. ¿Quieres cambiar algún plato? "))
        
            
    print("Genial! Nos alegramos de que te guste tu menú. Esta es tu lista de la compra: ")

    return df