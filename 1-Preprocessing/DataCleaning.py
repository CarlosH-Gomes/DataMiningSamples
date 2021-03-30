import pandas as pd
import numpy as np

def main():
    names =['date','quarter','department','day','team','targeted_productivity','smv','wip','over_time','incentive','idle_time','idle_men','no_of_style_change','no_of_workers','actual_productivity'] # Nome das colunas 
    features  = ['date','quarter','department','day','team','targeted_productivity','smv','wip','over_time','incentive','idle_time'] # Define as colunas que serão  utilizadas
    output_file = '0-Datasets/garments_worker_productivityClear.data'
    input_file = '0-Datasets/garments_worker_productivity.csv'
    df = pd.read_csv(input_file, # Nome do arquivo com dados
                     names = names, # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values='?') # Define que ? será considerado valores ausentes
    
    df_original = df.copy()
    # Imprime as 15 primeiras linhas do arquivo
    print("PRIMEIRAS 15 LINHAS\n")
    print(df.head(15))
    print("\n")        

    # Imprime informações sobre dos dados
    print("INFORMAÇÕES GERAIS DOS DADOS\n")
    print(df.info())
    print("\n")
    
    # Imprime uma analise descritiva sobre dos dados
    print("DESCRIÇÃO DOS DADOS\n")
    print(df.describe())
    print("\n")
    
    # Imprime a quantidade de valores faltantes por coluna
    print("VALORES FALTANTES\n")
    print(df.isnull().sum())
    print("\n")
    
    # Tratando valores faltantes da coluna team
    print("VALORES FALTANTES DA COLUNA team\n")
    print('Total valores ausentes: ' + str(df['team'].isnull().sum()))

    
    columns_missing_value = df.columns[df.isnull().any()]
    print(columns_missing_value)
    method = 'mode' # number or median or mean or mode
    
    for c in columns_missing_value:
        UptateMissingvalue(df, c)
    
    print('Total valores ausentes: ' + str(df['team'].isnull().sum()))
    print(df.describe())
    print("\n")
    print(df.head(15))
    print(df_original.head(15))
    print("\n")
    
    # Salva arquivo com o tratamento para dados faltantes
    df.to_csv(output_file, header=False, index=False)  
    

def UptateMissingvalue(df, column, method="mode", number=0):
    if method == 'number':
        # Substituindo valores ausentes por um número
        df[column].fillna(number, inplace=True)
    elif method == 'median':
        # Substituindo valores ausentes pela mediana 
        median = df['team'].median()
        df[column].fillna(median, inplace=True)
    elif method == 'mean':
        # Substituindo valores ausentes pela média
        mean = df[column].mean()
        df[column].fillna(mean, inplace=True)
    elif method == 'mode':
        # Substituindo valores ausentes pela moda
        mode = df[column].mode()[0]
        df[column].fillna(mode, inplace=True)


if __name__ == "__main__":
    main()