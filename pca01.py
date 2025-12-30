import pandas as pd
import sklearn 
import matplotlib.pyplot as plt
import time as time

from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    
    dt_heart = pd.read_csv('./data/heart.csv')

    print(dt_heart.head(1))
   
    dt_features  = dt_heart.drop(['target'], axis=1)
    dt_target = dt_heart['target']
    print(dt_features.head(1))
    start = time.time()
    dt_features = StandardScaler().fit_transform(dt_features)
      
    print("despues :" , dt_features[:1])

    X_train, X_test, y_train, y_test = train_test_split(dt_features, dt_target, test_size=0.3, random_state=42)
    end = time.time()   
    print(f"el tiempo de arranque es  {start} y el salida {end} tardando :: {end-start}")
#preparacion_datos_pca
# Clase 11 de 37
    print(X_train.shape)
    print(y_train.shape)
    print(X_test.shape)
    print(y_test.shape)
    #sin datos de components=min(numero de muestras , n_features)
    pca = PCA(n_components=3)
    pca.fit(X_train)
    
    #excelente si tenes computador con bajos recursos.
    ipca = IncrementalPCA(n_components=3,batch_size=10)
    ipca.fit(X_train)
    
    