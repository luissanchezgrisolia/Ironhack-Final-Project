import pandas as pd
import matplotlib.pyplot as plt

def to_png(df):
    """
    Df to a image
    """
    df_table=df.T.reset_index() 
    df_table=df_table["index"].astype(str)+ "    "+ df_table[0].astype(str) 
    df_table=pd.DataFrame(df_table)
    table = df_table


    # table
    plt.subplot(121)

    cell_text = []

    for row in range(len(table)):
        cell_text.append(table.iloc[row])


    plt.table(cellText=cell_text, colLabels="Ingredientes", loc='center')
    plt.axis('off')


    plt.savefig("body.png", bbox_inches='tight') 

    return 