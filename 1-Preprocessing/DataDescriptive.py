import pandas as pd
import numpy as np


def main():
     # Faz a leitura do arquivo
    names =['date','quarter','department','day','team','targeted_productivity','smv','wip','over_time','incentive','idle_time','idle_men','no_of_style_change','no_of_workers','actual_productivity','productivity'] # Nome das colunas 
    features  = ['targeted_productivity','smv','over_time','incentive','actual_productivity'] # Define as colunas que serão  utilizadas
    input_file = '0-Datasets/garments_worker_productivityClear.data'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                    usecols = features,
                     names = names) # Nome das colunas   
    
    #media 
    print('Média')
    print(df.mean())
    print('\n\n')

    #median
    print('Mediana')
    print(df.median())
    print('\n\n')

    #quatil
    print('Quantil')
    print(df.quantile())
    print('\n')
    print('Quantil 25%')
    print(df.quantile(q=0.25))
    print('\n\n')

    #moda
    print('Moda')
    print(df.mode())
    print('\n\n')


    #Medidas de dispersãp
    # Amplitude
    print('Amplitude')
    ampl = df.max() - df.min()
    print(ampl)
    print('\n\n')

    #Variância
    print('Variância')
    print(df.var())
    print('\n\n')

    #Desvio Padrão
    print('Desvio padrão')
    print(df.std())
    print('\n\n')

    #Desvio absoluto
    print('Desvio absoluto')
    print(df.mad())
    print('\n\n')

    #Covariância e Correlação
    print('Covariância')
    print(df.cov())
    print('\n')
    print('Correlação')
    print(df.corr())
    print('\n')

if __name__ == "__main__":
    main()