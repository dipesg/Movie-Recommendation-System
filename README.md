# Project: Movie Recommender System Using Machine Learning!

![movie_title](https://user-images.githubusercontent.com/75604769/163835573-52bbb215-2ca0-48ad-b610-57a9aae4750a.jpg)

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

# About this project:

This is a streamlit web application that can recommend various kinds of similar movies based on an user interest.
here is a demo,

* [App Link](https://movie-recommender7.herokuapp.com/)


# Demo:

![movie1](https://user-images.githubusercontent.com/75604769/163835579-3a4968fd-39f5-4219-b148-fb5cc8c17069.png)

![movie2](https://user-images.githubusercontent.com/75604769/163835584-89e85a93-8b60-4dee-a559-30e38ebf0c4b.png)

![movie3](https://user-images.githubusercontent.com/75604769/163835590-75fc2a4f-6e66-46aa-85bf-84d529eb4f86.png)


# Dataset has been used:

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/dipesg/Movie-Recommendation-System.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n movie python=3.7.10 -y
```

```bash
conda activate movie
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
#run this file to generate the models

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

