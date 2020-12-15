#Importación de librerías
import pandas as pd
import os, os.path
import matplotlib.pyplot as plt
from pandas.plotting import table


#Devuelve agenda vacía con columnas solicitadas [Dataframe]
def EmptyTableCreate(*cols):
    return pd.DataFrame(columns=list(cols), index=[0])

#Insertar valores. Devuelve dataframe con valores insertados
def InsertValues(df, value, cols):

    '''
    Versión poco eficiente

    dictCreate = {element: value for element in cols}
    colsDict = list(map(dict, zip(list(dictCreate.items())[::],\
         list(dictCreate.items())[::1])))
    df2 = df.append(*colsDict)
    return df2
    '''
    dictCreate = {element: [value] for element in cols}
    dfMod = df.append(pd.DataFrame(dictCreate),ignore_index=True).dropna(how="all")
    return dfMod

#Elimina filas o columnas especificadas. Devuelve dataframe con eliminación aplicada.
def DropValues(df, selection, colsMode=0):
    df.drop(selection, axis=colsMode, inplace=True)
    return df

#Modifica valores especificados. Devuelve dataframe con camvios aplicados.
def ModValues (df, selection, value):
    df.at[int(selection[0]), selection[1]] = value
    return df

#Ordena valores especificados. Devuelve dataframe ordenado:
def sortValues(df,cols):
    df.sort_values(by=cols, inplace=True)
    return df

#Genera archivo con el dataframe dado. 
#Excel = True --> Archivo[numero].xls
#CSV = True --> Archivo[numero].csv
#PNG = True --> Image[numero].png
def GenerateOutput(df, excel=False, csv=False, png=True):
    if csv==True:
        csvCounter = len([name for name in os.listdir("output/") if name.endswith(".csv")]) if os.listdir != 0 else 0
        df.to_csv(f"output/CSV{csvCounter+1}.csv")
        message = f"Archivo generado como CSV{csvCounter+1}"

    elif excel ==True:
        excelCounter = len([name for name in os.listdir("output/") if name.endswith(".xlsx")]) if os.listdir != 0 else 0
        print("OK")
        df.to_excel(f"output/Excel{excelCounter+1}.xlsx")
        message = f"Archivo generado como Excel{excelCounter+1}"
    
    if png == True:
        pngCounter = len([name for name in os.listdir("output/") if name.endswith(".png")]) if os.listdir != 0 else 0
        
        ax = plt.subplot(111, frame_on=False)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        table(ax, df)
        plt.savefig(f'output/Image{pngCounter+1}.png')

    return message

#Devuelve lista con strings. Evita problemas de comas.
def FormatInput(userInput):
    return userInput.replace(', ', ',').replace(' ,',',').split(",")
