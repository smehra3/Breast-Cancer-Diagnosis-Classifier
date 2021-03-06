import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

print(cancer.DESCR) # Print the data set description


# The object returned by `load_breast_cancer()` is a scikit-learn Bunch object, which is similar to a dictionary.

cancer.keys()


type(cancer)
np.column_stack((cancer.data, cancer.target))


# ### Question 0 (Example)
# 
# How many features does the breast cancer dataset have?
# 
# *This function should return an integer.*

def answer_zero():
    # This function returns the number of features of the breast cancer dataset, which is an integer. 
    return len(cancer['feature_names'])

answer_zero()


# ### Question 1
# 
# Scikit-learn works with lists, numpy arrays, scipy-sparse matrices, and pandas DataFrames, so converting the dataset to a DataFrame is not necessary for training this model. Using a DataFrame does however help make many things easier such as munging data, so let's practice creating a classifier with a pandas DataFrame. 
# 
# 
#
# *columns = *
# 
#     ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
#     'mean smoothness', 'mean compactness', 'mean concavity',
#     'mean concave points', 'mean symmetry', 'mean fractal dimension',
#     'radius error', 'texture error', 'perimeter error', 'area error',
#     'smoothness error', 'compactness error', 'concavity error',
#     'concave points error', 'symmetry error', 'fractal dimension error',
#     'worst radius', 'worst texture', 'worst perimeter', 'worst area',
#     'worst smoothness', 'worst compactness', 'worst concavity',
#     'worst concave points', 'worst symmetry', 'worst fractal dimension',
#     'target']
# 
# *and index = *
# 
#     RangeIndex(start=0, stop=569, step=1)

def answer_one():
    
    # Your code here
    return pd.DataFrame(np.column_stack((cancer.data, cancer.target)), columns = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
    'mean smoothness', 'mean compactness', 'mean concavity',
    'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error',
    'smoothness error', 'compactness error', 'concavity error',
    'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area',
    'worst smoothness', 'worst compactness', 'worst concavity',
    'worst concave points', 'worst symmetry', 'worst fractal dimension',
    'target'], index = pd.RangeIndex(start=0, stop=569, step=1))# Return your answer


# ### Question 2
# What is the class distribution? (i.e. how many instances of `malignant` (encoded 0) and how many `benign` (encoded 1)?)

def answer_two():
    cancerdf = answer_one()
    
    # Your code here
    df = answer_one()
    df['malignant'] = df[df.target==0.0].size
    df['benign'] = df[df.target==1.0].size
    #target = df[['malignant','benign']]
    #print(target.values[0])
    #print(pd.Series(data = target.values[0], index = ['malignant', 'benign']))
    return pd.Series(data = df[['malignant','benign']].values[0], index = ['malignant', 'benign'])# Return your answer



# ### Question 3
# Split the DataFrame into `X` (the data) and `y` (the labels).

def answer_three():
    cancerdf = answer_one()
    # Your code here
    X = cancerdf[cancer['feature_names']]
    y = cancerdf['target']
    return X, y


# ### Question 4
# Using `train_test_split`, split `X` and `y` into training and test sets `(X_train, X_test, y_train, and y_test)`.

from sklearn.model_selection import train_test_split

def answer_four():
    X, y = answer_three()
    
    # Your code here
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    return X_train, X_test, y_train, y_test


# ### Question 5
# Using KNeighborsClassifier, fit a k-nearest neighbors (knn) classifier with `X_train`, `y_train` and using one nearest neighbor (`n_neighbors = 1`).

from sklearn.neighbors import KNeighborsClassifier

def answer_five():
    X_train, X_test, y_train, y_test = answer_four()
    
    # Your code here
    classifier = KNeighborsClassifier(n_neighbors = 1)
    return classifier.fit(X_train, y_train)# Return your answer


# ### Question 6
# Using your knn classifier, predict the class label using the mean value for each feature.

def answer_six():
    cancerdf = answer_one()
    means = cancerdf.mean()[:-1].values.reshape(1, -1)
    # Your code here
    knn = answer_five()
    return knn.predict(means)# Return your answer


# ### Question 7
# Using your knn classifier, predict the class labels for the test set `X_test`.

def answer_seven():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()
    
    # Your code here
    
    return knn.predict(X_test)# Return your answer


# ### Question 8
# Find the score (mean accuracy) of your knn classifier using `X_test` and `y_test`.
# In[22]:

def answer_eight():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()
    
    # Your code here
    
    return knn.score(X_test, y_test)# Return your answer


def accuracy_plot():
    import matplotlib.pyplot as plt

    get_ipython().magic('matplotlib notebook')

    X_train, X_test, y_train, y_test = answer_four()

    # Find the training and testing accuracies by target value (i.e. malignant, benign)
    mal_train_X = X_train[y_train==0]
    mal_train_y = y_train[y_train==0]
    ben_train_X = X_train[y_train==1]
    ben_train_y = y_train[y_train==1]

    mal_test_X = X_test[y_test==0]
    mal_test_y = y_test[y_test==0]
    ben_test_X = X_test[y_test==1]
    ben_test_y = y_test[y_test==1]

    knn = answer_five()

    scores = [knn.score(mal_train_X, mal_train_y), knn.score(ben_train_X, ben_train_y), 
              knn.score(mal_test_X, mal_test_y), knn.score(ben_test_X, ben_test_y)]


    plt.figure()

    # Plot the scores as a bar chart
    bars = plt.bar(np.arange(4), scores, color=['#4c72b0','#4c72b0','#55a868','#55a868'])

    # directly label the score onto the bars
    for bar in bars:
        height = bar.get_height()
        plt.gca().text(bar.get_x() + bar.get_width()/2, height*.90, '{0:.{1}f}'.format(height, 2), 
                     ha='center', color='w', fontsize=11)

    # remove all the ticks (both axes), and tick labels on the Y axis
    plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

    # remove the frame of the chart
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.xticks([0,1,2,3], ['Malignant\nTraining', 'Benign\nTraining', 'Malignant\nTest', 'Benign\nTest'], alpha=0.8);
    plt.title('Training and Test Accuracies for Malignant and Benign Cells', alpha=0.8)


accuracy_plot()



