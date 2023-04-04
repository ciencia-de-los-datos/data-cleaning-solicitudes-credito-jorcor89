"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():


    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df.reset_index(inplace=True,drop=True)

    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],dayfirst=True)

    df.dropna(axis='index',inplace=True)
    df.drop_duplicates(inplace=True)

    df['sexo'] = df['sexo'].str.lower().astype(str).str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.lower().astype(str)
    df['barrio'] = df['barrio'].str.lower().astype(str)
    df['línea_credito'] = df['línea_credito'].str.lower().astype(str)
        
    df['idea_negocio'] = df['idea_negocio'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['barrio'] = df['barrio'].str.replace('_','-').str.replace('-',' ')
    df['línea_credito'] = df['línea_credito'].str.replace('_',' ').str.replace('-',' ').str.strip()

    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','',regex=False).str.replace(' ','').str.strip().astype(float)   

    df.drop_duplicates(inplace=True)
    df.dropna(axis='index',inplace=True)
    
    return df