import pandas as pd

#importando o arquivo com os dados para manipular.
dataframe = pd.read_csv('dataframe_yuri_xiaomi_x5.csv')

#filtrar as colunas Directions correspondentes à norte.
dataframe_filtrado  = dataframe[dataframe["Direction"]=="norte"]

#eliminar as colunas Direction, Alpha, Beta, Gama, X, Y, Device, Brand, Model e Created das linhas.
dataframe_filtrado = dataframe_filtrado.drop(columns=["Direction", "Alpha", "Beta", "Gama", "X", "Y", "Device", "Brand", "Model", "Created"])

#printar apenas as 10 linhas do arquivo filtrado e quantas linhas o novo dataframe possui:
print(dataframe_filtrado.head(10))
print(len(dataframe_filtrado))

#salvar o arquivo modificado
dataframe_filtrado.to_csv("dataframe_filtrado", index=False)