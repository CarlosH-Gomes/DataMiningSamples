import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def main():
    # Faz a leitura do arquivo
    names =['date','quarter','department','day','team','targeted_productivity','smv','wip','over_time','incentive','idle_time','idle_men','no_of_style_change','no_of_workers','actual_productivity'] # Nome das colunas 
    features  = ['team','targeted_productivity','smv','wip','over_time','incentive','idle_time','actual_productivity'] # Define as colunas que serão  utilizadas
    input_file = '0-Datasets/garments_worker_productivityClear.data'
    target = 'no_of_workers'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    
    
    plt.title('')
    plt.xlabel('Número de trabalhadores em cada equipe')
    plt.ylabel('Frequência Absoluta')
    #rwidth é o tamanho relativo das barras. 
    plt.hist(df[target], 5, rwidth=0.9)
    plt.show()

    #Número de pessoas no time durante a semana
    plt.title('Número de pessoas no time durante a semana')
    dados = df.groupby(['day']).no_of_workers.mean()
    plt.plot(dados)
    plt.show()

   
    #produtividade dias da semana
    plt.title('Produtividade dias da semana')
    dados = df.groupby(['day']).actual_productivity.mean()
    plt.plot(dados)
    plt.show()


    #grafico comparativo produtividade baseado nos dias da semana de cada departamento
    plt.title('Produtividade  baseado nos dias da semana de cada departamento')
    dados = df.groupby(['day','department']).actual_productivity.mean()
    dados = dados.reset_index()
    y1 = dados.copy()
    y2 = dados.copy()
    indexY1 = y1[ y1['department'] == 'finishing' ].index
    y1.drop(indexY1 , inplace=True)
    indexY2 = y2[ y2['department'] == 'sweing' ].index
    y2.drop(indexY2 , inplace=True)
    
    x1 =  np.arange(len(y1['actual_productivity']))
    x2 = [x + 0.25 for x in x1]

    plt.bar(x1, y1['actual_productivity'],  width=0.25, label = 'finishing', color = 'b')
    plt.bar(x2, y2['actual_productivity'],  width=0.25, label = 'sweing', color = 'y')
    plt.legend()
    plt.xticks([x + 0.25 for x in range(len( y1['actual_productivity']))], y2['day'])
    plt.show()

    #grafico pizza produtividade
    plt.title('Produtividade Departamentos')
    labels = ['Costura', 'Acabamento']
    pizza = dados.groupby(['department']).actual_productivity.mean()
    plt.pie(pizza, autopct='%0.1f%%', pctdistance=1.15, labels=labels)
    plt.show()

    dados = df.groupby(['date']).actual_productivity.mean()
    dados = dados.reset_index()
    plt.plot(dados['actual_productivity'])
    plt.show()


if __name__ == "__main__":
    main()