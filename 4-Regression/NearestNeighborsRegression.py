import pandas as pd
from sklearn.datasets import load_boston 
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# carrega os dados
names =['date','quarter','department','day','team','targeted_productivity','smv','wip','over_time','incentive','idle_time','idle_men','no_of_style_change','no_of_workers','actual_productivity','productivity'] # Nome das colunas 
features  = ['targeted_productivity','team','wip','smv','over_time','incentive','no_of_workers','actual_productivity'] # Define as colunas que serão  utilizadas
input_file = '0-Datasets/garments_worker_productivityClear.data'
df = pd.read_csv(input_file,    # Nome do arquivo com dados
                  usecols = features,
                  names = names) # Nome das colunas   


    # Separate X and y data
X = df.drop('actual_productivity', axis=1)
y = df.actual_productivity  
print(df.head()) 


# separa em set de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

regr = KNeighborsRegressor(n_neighbors=2)
regr.fit(X_train, y_train)

r2_train = regr.score(X_train, y_train)
r2_test = regr.score(X_test, y_test)
print('R2 no set de treino: %.2f' % r2_train)
print('R2 no set de teste: %.2f' % r2_test)

y_pred = regr.predict(X_test)
abs_error = mean_absolute_error(y_pred, y_test)
print('Erro absoluto no set de treino: %.2f' % abs_error)