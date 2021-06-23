import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def main():
    # Faz a leitura do arquivo
    names =['date','quarter','department','day','team','targeted_productivity','smv','wip','over_time','incentive','idle_time','idle_men','no_of_style_change','no_of_workers','actual_productivity','productivity'] # Nome das colunas 
    features  = ['team','targeted_productivity','smv','wip','over_time','incentive','idle_time','actual_productivity'] # Define as colunas que serão  utilizadas
    input_file = '0-Datasets/garments_worker_productivityClear.data'
    target = 'no_of_workers'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    

    
    plt.title('')
    plt.xlabel('Produtividade')
    plt.ylabel('Frequência Absoluta')
    #rwidth é o tamanho relativo das barras. 
    plt.hist(df['targeted_productivity'], 8, rwidth=0.9)
    plt.show()


     #Número de pessoas no time durante a semana no_of_workers
    organiza = pd.DataFrame({
             'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Saturday', 'Sunday'],
             'num': [0, 1, 2, 3, 4, 5]})

    plt.title('Produtividade dias da semana')
    dados = df.groupby(['day']).actual_productivity.mean()
    dados = pd.merge(dados, organiza, on='day')
    dados = dados.sort_values('num')
    dados2 = df.groupby(['day']).targeted_productivity.mean()
    dados2 = pd.merge(dados2, organiza, on='day')
    dados2 = dados2.sort_values('num')
    plt.plot(dados['day'],dados['actual_productivity'],'g',label='Produtividade')
    plt.plot(dados2['day'],dados2['targeted_productivity'],'b',label='Produtividade atribuida')
    plt.legend()
    plt.grid()
    
    plt.show()
   
    #Número de pessoas no time durante a semana no_of_workers
    plt.title('Número de pessoas no time durante a semana')
    dados = df.groupby(['day','department']).no_of_workers.mean()
    dados = dados.reset_index()
    print(dados)
    y1 = dados.copy()
    y2 = dados.copy()
    indexY1 = y1[ y1['department'] == 'finishing' ].index
    y1.drop(indexY1 , inplace=True)
    indexY2 = y2[ y2['department'] == 'sweing' ].index
    y2.drop(indexY2 , inplace=True)
    
    x1 =  np.arange(len(y1['no_of_workers']))
    x2 = [x + 0.25 for x in x1]
    print(dados)
    plt.bar(x1, y1['no_of_workers'],  width=0.25, label = 'finishing', color = 'b')
    plt.bar(x2, y2['no_of_workers'],  width=0.25, label = 'sweing', color = 'y')
    plt.legend()
    plt.xticks([x + 0.25 for x in range(len( y1['no_of_workers']))], y2['day'])
    plt.show()

   
       
    #produtividade dias da semana
    organiza = pd.DataFrame({
             'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Saturday', 'Sunday'],
             'num': [0, 1, 2, 3, 4, 5]})

    plt.title('Produtividade dias da semana')
    dados = df.groupby(['day']).actual_productivity.mean()
    dados = pd.merge(dados, organiza, on='day')
    dados = dados.sort_values('num')
    plt.plot(dados['day'],dados['actual_productivity'])
    plt.grid()
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

    #produtividade meses
    dados = df.groupby(['date']).actual_productivity.mean()
    dados = dados.reset_index()
    dados['date'] = pd.to_datetime(dados['date'])
    dadosOrdenados = dados.sort_values(by='date')
    print(dadosOrdenados)
    plt.figure(figsize=(15,8))
    plt.legend(['Produtividade'], loc = 'lower right', fontsize=15)
    plt.plot(dadosOrdenados['date'], dadosOrdenados['actual_productivity']) 
    plt.grid()
    plt.show()

    #produtividade meses comparativa
    dados = df.groupby(['date']).actual_productivity.mean()
    dados = dados.reset_index()
    dados['date'] = pd.to_datetime(dados['date'])
    dadosOrdenados = dados.sort_values(by='date')
    dados2 = df.groupby(['date']).targeted_productivity.mean()
    dados2 = dados2.reset_index()
    dados2['date'] = pd.to_datetime(dados2['date'])
    dadosOrdenados2 = dados2.sort_values(by='date')
   
    plt.figure(figsize=(15,8))
    plt.legend(['Produtividade'], loc = 'lower right', fontsize=15)
    plt.plot(dadosOrdenados['date'], dadosOrdenados['actual_productivity'],'g',label='Produtividade')
    plt.plot(dadosOrdenados2['date'],dadosOrdenados2['targeted_productivity'],'b',label='Produtividade atribuida')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()