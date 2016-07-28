# Project 1: Model Evaluation & Validation
## Predicting Boston Housing Prices


## Table of Contents  
- [Project Overview](#project-overview)
- [Project Highlights](#project-highlights)
- [Install](#install)
- [Code](#code)
- [Run](#run)
- [Data](#data)


### <a name="project-overview"></a>Project Overview

The Boston housing market is highly competitive, and you want to be the best real estate agent in the area. To compete with your peers, you decide to leverage a few basic machine learning concepts to assist you and a client with finding the best selling price for their home. Luckily, you’ve come across the Boston Housing dataset which contains aggregated data on various features for houses in Greater Boston communities, including the median value of homes for each of those areas. Your task is to build an optimal model based on a statistical analysis with the tools available. This model will then be used to estimate the best selling price for your clients' homes.

In this project, we will apply basic machine learning concepts on data collected for housing prices in the Boston, Massachusetts area to predict the selling price of a new home. We will first explore the data to obtain important features and descriptive statistics about the dataset. Next, we will properly split the data into testing and training subsets, and determine a suitable performance metric for this problem. We will then analyze performance graphs for a learning algorithm with varying parameters and training set sizes. This will enable we to pick the optimal model that best generalizes for unseen data. Finally, we will test this optimal model on a new sample and compare the predicted selling price to our statistics.


### <a name="project-highlights"></a>Project Highlights

This project is designed to get you acquainted to working with datasets in Python and applying basic machine learning techniques using `NumPy` and `scikit-learn`. Before being expected to use many of the available algorithms in the sklearn library, it will be helpful to first practice analyzing and interpreting the performance of your model.

Things you will learn by completing this project:

- How to use `NumPy` to explore the descriptive statistics and investigate the latent features of a dataset.
- How to use `scikit-learn` to define a performance metric and build a machine learning model.
- How to measure goodness of fit by interpretting coefficient of determination, R<sup>2</sup>.
- The importance of splitting the dataset into training and test sets and using k-fold cross validation.
- How to analyze learning curves and complexity curves for bias-variance tradeoff.
- How to determine the optimal model for predictions with grid search.
- How to evaluate a model’s performance and limitations by analyzing its sensitivity and applicabilities.
- How to visualize the pairwise relationships in a dataset with `Seaborn`.


### <a name="install"></a>Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/)

Udacity recommends our students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 


### <a name="code"></a>Code

Complete code is provided in the `boston_housing.ipynb` notebook file. You will also be required to use the included `visuals.py` Python file and the `housing.csv` dataset file to complete your work.


### <a name="run"></a>Run

In a terminal or command window, navigate to the top-level project directory `boston_housing/` (that contains this README) and run the following command:

```jupyter notebook boston_housing.ipynb```

This will open the Jupyter Notebook software and project file in your browser.


### <a name="data"></a>Data

The dataset used in this project is included with the scikit-learn library ([`sklearn.datasets.load_boston`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston)).

It contains the following attributes for each housing area, including median value (which you will try to predict):

- `CRIM`: per capita crime rate by town
- `ZN`: proportion of residential land zoned for lots over 25,000 sq.ft.
- `INDUS`: proportion of non-retail business acres per town
- `CHAS`: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- `NOX`: nitric oxides concentration (parts per 10 million)
- `RM`: average number of rooms per dwelling
- `AGE`: proportion of owner-occupied units built prior to 1940
- `DIS`: weighted distances to five Boston employment centres
- `RAD`: index of accessibility to radial highways
- `TAX`: full-value property-tax rate per $10,000
- `PTRATIO`: pupil-teacher ratio by town
- `B`: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- `LSTAT`: % lower status of the population
- `MEDV`: Median value of owner-occupied homes in $1000's

You do not have to download it separately. You can find more information on this dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing) page.
