import pandas as pd
import numpy as np
from scipy.stats import randint, expon

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.externals import joblib
from sklearn import metrics

# Models
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier


def prepare_data():
    df = pd.read_csv('content/data/data.csv', index_col=[0])

    # Selecting TEA column as target and dropping it
    target = df['TEA']
    df.drop(['TEA'], axis=1, inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.2, random_state=13)
    return X_train, X_test, y_train, y_test, df.columns


def print_metrics(model, test_values, preds):
    print('{0} accuracy: {1:.4f}'.format(model, metrics.accuracy_score(test_values, preds)))
    print('{0} precision: {1:.4f}'.format(model, metrics.precision_score(test_values, preds)))
    print('{0} recall: {1:.4f}'.format(model, metrics.recall_score(test_values, preds)))


def report(results, n_top=3):
    for i in range(1, 2):#, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")


def choose_svm(X_train, X_test, y_train, y_test):
    print('********************************************')
    print('Training model: SVM')
    print('********************************************')

    param_dist = {
        'C': [i for i in range(1,100,10)],
        'gamma': [i for i in np.arange(0.1,1,0.1)],
        'kernel': ['rbf'],
        'class_weight':['balanced', None]
    }

    random_search = GridSearchCV(
        estimator=svm.SVC(),
        param_grid=param_dist,
        verbose=True
    )

    random_search.fit(X_train, y_train)
    report(random_search.cv_results_)

    # Building and training the best estimator
    model_svm = random_search.best_estimator_
    model_svm.fit(X_train, y_train)
    svm_y_pred = model_svm.predict(X_test)
    #joblib.dump(model_svm, 'content/models/model_svm.pkl')

    print_metrics('SVM', y_test, svm_y_pred)


def choose_decision_tree(X_train, X_test, y_train, y_test):
    print('********************************************')
    print('Training model: Decision tree')
    print('********************************************')

    param_dist = {
        "max_depth": [3, 5, None],
        "max_features": [i for i in range(1,11)],
        "min_samples_leaf": [i for i in range(1,11)],
        "criterion": ["gini", "entropy"]
    }

    random_search = GridSearchCV(
        estimator=DecisionTreeClassifier(random_state=42),
        param_grid=param_dist,
        verbose=True
    )

    random_search.fit(X_train, y_train)
    report(random_search.cv_results_)

    # Building and training the best estimator
    model_tree = random_search.best_estimator_
    model_tree.fit(X_train, y_train)
    tree_y_pred = model_tree.predict(X_test)
    #joblib.dump(model_tree, 'content/models/model_tree.pkl')

    print_metrics('Decision Tree', y_test, tree_y_pred)


def choose_random_forest(X_train, X_test, y_train, y_test):
    print('********************************************')
    print('Training model: Random forest')
    print('********************************************')

    param_dist = {'n_estimators': [400, 800, 1000],
                'max_features': ['auto', 'sqrt'],
                'max_depth': [40, 60, 80, 100, None],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
    }

    random_search = GridSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_grid=param_dist,
        verbose=True
    )

    random_search.fit(X_train, y_train)
    report(random_search.cv_results_)

    # Building and training the best estimator
    model_forest = random_search.best_estimator_
    model_forest.fit(X_train, y_train)
    forest_y_pred = model_forest.predict(X_test)
    #joblib.dump(model_forest, 'content/models/model_forest.pkl')

    print_metrics('Random Forest', y_test, forest_y_pred)


def choose_knn(X_train, X_test, y_train, y_test):
    print('********************************************')
    print('Training model: KNN')
    print('********************************************')

    param_dist = {'n_neighbors':[5,7,10],
                'leaf_size':[1,3,5],
                'weights':['uniform', 'distance'],
                'algorithm':['auto', 'kd_tree']
    }

    random_search = GridSearchCV(
        estimator=KNeighborsClassifier(),
        param_grid=param_dist,
        verbose=True
    )

    random_search.fit(X_train, y_train)
    report(random_search.cv_results_)

    # Building and training the best estimator
    model_knn = random_search.best_estimator_
    model_knn.fit(X_train, y_train)
    knn_y_pred = model_knn.predict(X_test)
    #joblib.dump(model_knn, 'content/models/model_knn.pkl')

    print_metrics('K Nearest Neighbors', y_test, knn_y_pred)


def choose_neural_network(X_train, X_test, y_train, y_test):
    print('********************************************')
    print('Training model: Neural network')
    print('********************************************')

    param_dist = {'activation': ['tanh', 'relu'],
                'alpha': [0.0001, 0.001, 0.01],
                'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
                'learning_rate': ['constant','adaptive'],
                'solver': ['sgd', 'adam'],
    }

    random_search = GridSearchCV(
        estimator=MLPClassifier(random_state=42),
        param_grid=param_dist,
        verbose=True
    )

    random_search.fit(X_train, y_train)
    report(random_search.cv_results_)

    # Building and training the best estimator
    model_neural = random_search.best_estimator_
    model_neural.fit(X_train, y_train)
    neural_y_pred = model_neural.predict(X_test)
    #joblib.dump(model_neural, 'content/models/model_neural.pkl')

    print_metrics('Neural Network', y_test, neural_y_pred)


def build_model():
    X_train, X_test, y_train, y_test, columns = prepare_data()

    model_forest = RandomForestClassifier(random_state=42, max_depth=40, max_features='auto',
             min_samples_leaf=1, min_samples_split=2, n_estimators=400)

    model_forest.fit(X_train, y_train)
    forest_y_pred = model_forest.predict(X_test)
    joblib.dump(model_forest, 'content/models/model_forest.pkl')

    print_metrics('Random Forest', y_test, forest_y_pred)

    for name, score in zip(columns, model_forest.feature_importances_):
        print(name, score)
