"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    #
    # Inserte su código aquí
    #

    #cargar el archivo y eliminar columna que no sirve
    df = pd.read_csv("solicitudes_credito.csv", sep=";").drop(columns=['Unnamed: 0'])
    
    #eliminar duplicados y nulos
    df = df.dropna().drop_duplicates()

    #normalizar las columnas
    normalize_str = lambda x: x.lower().replace('_', ' ').replace('-', ' ').strip()
    #sexo
    df['sexo'] = df['sexo'].apply(normalize_str)
    #tipo emprendimiento
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(normalize_str)
    #idea negocio
    df['idea_negocio'] = df['idea_negocio'].apply(normalize_str)
    #linea credito
    df['línea_credito'] = df['línea_credito'].apply(normalize_str)
    
    #modiciaciones columna barrio reemplazamos _ por - y luego -
    df['barrio'] = df['barrio'].apply(lambda x: x.lower().replace('_', '-').replace('-', ' '))

    #convertir monto del credito a número
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '').str.replace('$', '', regex=False).str.replace(' ', '').astype(float)
    
    #cambiar el formato de la fecha de la columna fecha de beneficio
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True)
    
    #eliminar duplicados y nulos
    df = df.drop_duplicates().dropna()
    
    return df