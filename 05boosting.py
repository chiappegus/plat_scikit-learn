import pandas as pd
import sklearn



import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    
    dt_heart = pd.read_csv('./data/heart.csv')

    print(dt_heart['target'].describe())

    X = dt_heart.drop(['target'], axis=1)
    y = dt_heart['target']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

    boost = GradientBoostingClassifier(n_estimators=50).fit(X_train, y_train)
    boost_pred = boost.predict(X_test)
    print("="*64)
    print(accuracy_score(boost_pred, y_test))
    
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.35)

    estimators = range(10, 200, 10)
    total_accuracy = []
    for i in estimators:
        boost = GradientBoostingClassifier(n_estimators=i).fit(X_train, y_train)
        boost_pred = boost.predict(X_test)

        total_accuracy.append(accuracy_score(y_test, boost_pred))
    
    plt.plot(estimators, total_accuracy)
    plt.xlabel('Estimators')
    plt.ylabel('Accuracy')
    plt.show()
    plt.savefig('Boost.png')

    print(np.array(total_accuracy).max())

#implementacion_boosting