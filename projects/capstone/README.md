# Capstone Project
## Di-Tech: Forecasting Supply and Demand Gap for Didi


## Table of Contents  
- [Project Overview](#project-overview)
- [Project Highlights](#project-highlights)
- [Install](#install)
- [Code](#code)
- [Run](#run)
- [Data](#data)


### <a name="project-overview"></a>Project Overview

Didi Chuxing, the dominant ride-hailing company covering more than 400 cities across China, processes over 11 million trips, plans over 9 billion routes and collects over 50TB of data per day. For this challenge, Di-Tech provides 600MB of its real world data on order information, traffic jam level, weather measurements and points of interest. The goal is to predict the supply and demand gap for a specific area over a certain period of time. With this knowledge on the gap between requested and unanswered order, the company can improve their driver-rider match and enhance service reliability.


### <a name="project-highlights"></a>Project Highlights

This project is an attempt to solving the [Di-Tech challenge](http://research.xiaojukeji.com/competition/main.action?competitionId=DiTech2016) with [XGBoost](https://xgboost.readthedocs.io/en/latest/).

Things I've learned and accomplished by completing this project:

- How to load large datasets from multiple files in different directories.
- Processed and cleaned real-world data.
- Built a regression model with XGBoost that ranked top 20% on a leaderboard of 1500+.


### <a name="install"></a>Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [XGBoost](https://xgboost.readthedocs.io/en/latest/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/)

Udacity recommends our students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 


### <a name="code"></a>Code

Data Processing code is provided in the Jupyter notebook `data_processing.ipynb`. Data Analysis and Model Building code is provided in the Jupyter notebook `model_building.ipynb`. 


### <a name="run"></a>Run

In a terminal or command window, navigate to the top-level project directory then move to `/code/` directory and run the following command:

```jupyter notebook data_processing.ipynb```
and
```jupyter notebook model_building.ipynb```

This will open the Jupyter Notebook software and project file in your browser.


### <a name="data"></a>Data

Upon completion of the this project, the dataset has been updated by Di-Tech. The final round dataset of the Di-Tech Challenge can be downloaded [here](http://research.xiaojukeji.com/competition/detail.action?competitionId=DiTech2016). Due to the large size, if you want the first round dataset we are using in this project, please contact me and I will send it to you.

