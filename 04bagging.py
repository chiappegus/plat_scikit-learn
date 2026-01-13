import pandas as pd

from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import BaggingClassifier



  


from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score



from sklearn.svm import LinearSVC

from sklearn.svm import SVC

from sklearn.linear_model import SGDClassifier

from sklearn.tree import DecisionTreeClassifier


if __name__ == "__main__":

    dt_heart = pd.read_csv('./data2/heart.csv')

    print(dt_heart['target'].describe())
    print("*"*99)
    print("*"*99)
    print("*"*99)
    # print(dt_heart.describe())
    print("*"*99)
    print("*"*99)
    print("*"*99)
    X = dt_heart.drop(['target'], axis=1 )
    # print("*"*99)
    # print("*"*99)
    # print("*"*99)
    # print(dt_heart.describe())
    # print("*"*99)
    # print("*"*99)
    # print("*"*99)
    
    # dt_heart2=dt_heart.copy()
    
    # print("*"*99)
    # print("*"*99)
    # print("*"*99)
    # print(dt_heart2.describe())
    # print("*"*99)
    # print("*"*99)
    # print("*"*99)
    # X_ = dt_heart2.drop(['target'], axis=1 ,inplace=True )
    # print("*"*99)
    # print("*"*99)
    # print("*"*99)
    # print(dt_heart2.describe())
    # print("*"*99)
    # print("*"*99)
    # print("*"*99)
    # R = dt_heart.drop(['target'], inplace=True , axis=1)
    # print("*"*99)
    # print("*"*99)
    # print("*"*99)
    # print(dt_heart.describe())
    # print("*"*99)
    # print("*"*99)
    # print("*"*99)
    y = dt_heart['target']
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)
    
    
    
    print(''*99)
    print('*'*99)
    print('*'*99)
    print('*'*99)
    print('KNeighbors')
    knn_class = KNeighborsClassifier().fit(x_train, y_train)
    knn_pred = knn_class.predict(x_test)
    
    print('Accuracy KNeighbors:', accuracy_score(knn_pred, y_test))
   
    print('-'*99)
    print('-'*99)
    print('-'*99)
    print(''*99)



    print('*'*99)
    print('*'*99)
    print('*'*99)
    print('BAG_CLASS')
    bag_class = BaggingClassifier(KNeighborsClassifier(), n_estimators=50).fit(x_train, y_train)

    #bag_pred = bag_class.predict(x_test)
    bag_pred = bag_class.predict(x_test)
    
    print('Accuracy Bagging with KNeighbors:', accuracy_score(bag_pred, y_test))
 #bag_class = 
    print('-'*99)
    print('-'*99)
    print('-'*99)
    #prepacion_datos_bagging
    
    
    
    classifier = {

        'KNeighbors': KNeighborsClassifier(),
        'LinearSCV': LinearSVC(),
        'SVC': SVC(),
        'SGDC': SGDClassifier(),
        'DecisionTree': DecisionTreeClassifier()

    }



    for name, estimator in classifier.items():

        bag_class = BaggingClassifier(estimator, n_estimators=80).fit(x_train, y_train)

        bag_pred = bag_class.predict(x_test)



        print('Accuracy Bagging with {}:'.format(name), accuracy_score(bag_pred, y_test))

        print('')