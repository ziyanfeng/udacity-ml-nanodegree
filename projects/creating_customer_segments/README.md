# Project 3: Unsupervised Learning
## Creating Customer Segments

## Table of Contents  
- [Project Overview](#project-overview)
- [Project Highlights](#project-highlights)
- [Install](#install)
- [Code](#code)
- [Run](#run)
- [Data](#data)


### <a name="project-overview"></a>Project Overview

A wholesale distributor recently tested a change to their delivery method for some customers, by moving from a morning delivery service five days a week to a cheaper evening delivery service three days a week. Initial testing did not discover any significant unsatisfactory results, so they implemented the cheaper option for all customers. Almost immediately, the distributor began getting complaints about the delivery service change and customers were canceling deliveries — losing the distributor more money than what was being saved. You’ve been hired by the wholesale distributor to find what types of customers they have to help them make better, more informed business decisions in the future. Your task is to use unsupervised learning techniques to see if any similarities exist between customers, and how to best segment customers into distinct categories.

In this project we will apply unsupervised learning techniques on product spending data collected for customers of a wholesale distributor in Lisbon, Portugal to identify customer segments hidden in the data. We will first explore the data by selecting a small subset to sample and determine if any product categories highly correlate with one another. Afterwards, we will preprocess the data by scaling each product category and then identifying (and removing) unwanted outliers. With the good, clean customer spending data, we will apply PCA transformations to the data and implement clustering algorithms to segment the transformed customer data. Finally, we will compare the segmentation found with an additional labeling and consider ways this information could assist the wholesale distributor with future service changes.


### <a name="project-highlights"></a>Project Highlights

This project is designed to give you a hands-on experience with unsupervised learning and work towards developing conclusions for a potential client on a real-world dataset. Many companies today collect vast amounts of data on customers and clientele, and have a strong desire to understand the meaningful relationships hidden in their customer base. Being equipped with this information can assist a company engineer future products and services that best satisfy the demands or needs of their customers.

Things you will learn by completing this project:

- How to apply preprocessing techniques such as feature scaling and outlier detection.
- How to interpret data points that have been scaled, transformed, or reduced from PCA.
- How to analyze PCA dimensions and construct a new feature space.
- The strengths and weakness of K-means and GMM algorithms.
- How to optimally cluster a set of data to find hidden patterns in a dataset.
- How to assess information given by cluster data and use it in a meaningful way.


### <a name="install"></a>Install

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/)

Udacity recommends our students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 


### <a name="code"></a>Code

Template code is provided in the notebook `customer_segments.ipynb` notebook file. Additional supporting code can be found in `renders.py`. While some code has already been implemented to get you started, you will need to implement additional functionality when requested to successfully complete the project.


### <a name="run"></a>Run

In a terminal or command window, navigate to the top-level project directory `creating_customer_segments/` (that contains this README) and run the following command:

```jupyter notebook customer_segments.ipynb```

This will open the Jupyter Notebook software and project file in your browser.


## <a name="data"></a>Data

The dataset used in this project is included as `customers.csv`. You can find more information on this dataset on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers) page.
