# Project 0: Introduction and Fundamentals
## Titanic Survival Exploration


## Table of Contents  
- [Project Overview](#project-overview)
- [Project Highlights](#project-highlights)
- [Install](#install)
- [Code](#code)
- [Run](#run)
- [Data](#data)


### <a name='project-overview'></a>Project Overview

In this **_optional_** project, you will create decision functions that attempt to predict survival outcomes from the 1912 Titanic disaster based on each passenger’s features, such as sex and age. You will start with a simple algorithm and increase its complexity until you are able to accurately predict the outcomes for at least 80% of the passengers in the provided data. This project will introduce you to some of the concepts of machine learning as you start the Nanodegree program.


### <a name='project-highlights'></a>Project Highlights

This project is designed to get you started with Python and necessary packages to complete this project. There are two Python libraries, `NumPy` and `Pandas`, that we'll use a bit here in this project. Don't worry about how these libraries work for now — we'll get to them in more detail in later projects. 

Things you will learn by completing this project:

- How to install Python libraries.
- How to read `.csv` file into Pyhton with Pandas.
- How to use heuristics to make predictions.
- Have fun!


### <a name='install'></a>Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/)

If you already have Python 2.7 installed on your computer, then you can install `numpy`, `scikit-learn`, and Jupyter Notebook (formerly known as 'iPython Notebook') by using [`pip`](https://pip.pypa.io/en/stable/) on the command line. [This page](http://www.lfd.uci.edu/~gohlke/pythonlibs/) may also be of use for some packages for Windows users, if pip has trouble performing the installation. After installing pip, you can install all the packages with the following command:

`sudo pip install numpy pandas matplotlib jupyter scikit-learn`

Udacity recommends our students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.


### <a name='code'></a>Code

Template code is provided in the notebook `titanic_survival_exploration.ipynb` notebook file. Additional supporting code can be found in `titanic_visualizations.py`. While some code has already been implemented to get you started, you will need to implement additional functionality when requested to successfully complete the project.


### <a name='run'></a>Run

In a terminal or command window, navigate to the top-level project directory `titanic_survival_exploration/` (that contains this README) and run the following command:

```bash
jupyter notebook titanic_survival_exploration.ipynb
```


This will open the iPython Notebook software and project file in your web browser.


## <a name='data'></a>Data

The dataset used in this project is included as `titanic_data.csv`. This dataset is provided by Udacity and contains the following attributes:

- `survival` : Survival (0 = No; 1 = Yes)
- `pclass` : Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
- `name` : Name
- `sex` : Sex
- `age` : Age
- `sibsp` : Number of Siblings/Spouses Aboard
- `parch` : Number of Parents/Children Aboard
- `ticket` : Ticket Number
- `fare` : Passenger Fare
- `cabin` : Cabin
- `embarked` : Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
