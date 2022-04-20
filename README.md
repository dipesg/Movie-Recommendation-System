# Movie Recommender System

![movie_title](https://user-images.githubusercontent.com/75604769/163835573-52bbb215-2ca0-48ad-b610-57a9aae4750a.jpg)

## Table of Content
  
  * [Overview](#overview)
  * [Demo](#demo)
  * [Architechture](#architechture)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)

## Overview
The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. 

## About this project:
This is a streamlit web application that can recommend various kinds of similar movies based on an user interest.

## Demo:
[App Link](https://movie-recommender7.herokuapp.com/)



![movie1](https://user-images.githubusercontent.com/75604769/163835579-3a4968fd-39f5-4219-b148-fb5cc8c17069.png)

![movie2](https://user-images.githubusercontent.com/75604769/163835584-89e85a93-8b60-4dee-a559-30e38ebf0c4b.png)

![movie3](https://user-images.githubusercontent.com/75604769/163835590-75fc2a4f-6e66-46aa-85bf-84d529eb4f86.png)

## Architechture
![movie-archi](https://user-images.githubusercontent.com/75604769/163920958-f0074e01-6460-41fc-aa5d-84344973f4aa.png)


## Dataset 

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)



## Installation
#### STEPS:

Clone the repository

```bash
https://github.com/dipesg/Movie-Recommendation-System.git
```
##### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.7 -y
```

```bash
conda activate movie
```


##### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
##run this file to generate the pickle file.

generetingEmbedding.py
```

Now run,
```bash
streamlit run app.py
```


```bash
Author: Dipesh Silwal
Email: dipeshsilwal31@gmail.com

```

## Directory Tree
![tree1](https://user-images.githubusercontent.com/75604769/163923235-9d0f1256-13bb-4551-a571-d0fc3ebbd617.png)


![tree3](https://user-images.githubusercontent.com/75604769/163923667-2bc153bd-1c48-4661-8c77-9fd7376dd80e.png)


## Technologies Used
![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" width=170>](https://streamlit.io/) 
[<img target="_blank" src="https://numpy.org/images/logo.svg" width=270>](https://numpy.org/)  [<img target="_blank" src="https://pandas.pydata.org/static/img/pandas.svg" width=270>](https://pandas.pydata.org/about/citing.html)
