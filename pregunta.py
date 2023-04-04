"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():


    df = pd.read_csv("solicitudes_credito.csv", sep=";").drop(columns=['Unnamed: 0'])
    df = df.dropna().drop_duplicates()


    normalize_str = lambda x: x.lower().replace('_', ' ').replace('-', ' ').strip()
    df['sexo'] = df['sexo'].apply(normalize_str)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(normalize_str)
    df['idea_negocio'] = df['idea_negocio'].apply(normalize_str)
    df['línea_credito'] = df['línea_credito'].apply(normalize_str)
    df['barrio'] = df['barrio'].apply(lambda x: x.lower().replace('_', '-').replace('-', ' '))


    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '').str.replace('$', '', regex=False).str.replace(' ', '').astype(float)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'])
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%d/%m/%Y')
    #df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True)

    df = df.drop_duplicates().dropna()

    return df